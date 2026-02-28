from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.db.models import Q, F
from django.core.paginator import Paginator
from .models import Event, Registration, College

User = get_user_model()

# --- Public Views ---
def home(request):
    query = request.GET.get('q', '').strip()
    category_filter = request.GET.get('category', '').strip()
    
    # Filter based on Student's College or Global events
    if request.user.is_authenticated and not request.user.is_staff:
        events_queryset = Event.objects.filter(
            Q(college=request.user.college) | Q(is_global=True)
        )
    else:
        events_queryset = Event.objects.all()

    if query:
        events_queryset = events_queryset.filter(name__icontains=query)
    if category_filter:
        events_queryset = events_queryset.filter(category=category_filter)

    events_queryset = events_queryset.order_by('date')

    # Recommendation Logic
    all_events = list(events_queryset)
    if request.user.is_authenticated and hasattr(request.user, 'department'):
        all_events.sort(key=lambda x: x.category == request.user.department, reverse=True)

    # Pagination Logic
    paginator = Paginator(all_events, 6)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, 'home.html', {'events': events, 'query': query})

# --- Authentication Views ---
def student_signup(request):
    from .forms import StudentSignupForm
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = StudentSignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if hasattr(user, 'is_student') and user.is_student:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Access Denied: Use Admin Login.")
    else:
        form = AuthenticationForm()
    return render(request, 'student_login.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Access Denied: Admins only.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

# --- Profile and Dashboards ---
@login_required
def profile(request):
    user_registrations = Registration.objects.filter(user=request.user).order_by('-registered_at')
    return render(request, 'profile.html', {'registrations': user_registrations})

@login_required
def admin_dashboard(request):
    events = Event.objects.all().order_by('-date')
    student_count = User.objects.filter(is_student=True).count()
    total_registrations = Registration.objects.count()
    return render(request, 'events/admin_dashboard.html', {
        'events': events,
        'student_count': student_count,
        'total_registrations': total_registrations
    })

@login_required
def registered_students(request):
    registrations = Registration.objects.select_related('user', 'event').all().order_by('-registered_at')
    return render(request, 'events/registered_students.html', {'registrations': registrations})

# --- Event Detail and Registration ---
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    is_registered = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(user=request.user, event=event).exists()
    
    return render(request, 'detail.html', {
        'event': event, 
        'is_registered': is_registered
    })

@login_required
def register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if Registration.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, "Already registered!")
        return redirect('detail', event_id=event_id)

    if request.method == 'POST':
        from .forms import RegistrationForm
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.event, reg.user = event, request.user
            reg.save()
            # Update participant count
            Event.objects.filter(pk=event_id).update(participants=F('participants') + 1)
            messages.success(request, "Registration successful!")
            return redirect('profile')
    else:
        from .forms import RegistrationForm
        form = RegistrationForm(initial={'email': request.user.email})
    return render(request, 'event_register.html', {'form': form, 'event': event})