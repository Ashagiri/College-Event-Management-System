from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Event, Registration
from .forms import RegistrationForm, StudentSignupForm 

User = get_user_model()

# --- Public Views ---
def home(request):
    query = request.GET.get('q', '').strip() 
    if query:
        events = Event.objects.filter(name__icontains=query).order_by('date')
    else:
        events = Event.objects.order_by('date')
    return render(request, 'home.html', {'events': events, 'query': query})

# --- Student Views ---
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = StudentSignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Only allow users with is_student=True
            if user.is_student:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Access Denied: Use Admin Login.")
    else:
        form = AuthenticationForm()
    return render(request, 'student_login.html', {'form': form})

@login_required(login_url='student_login') 
def profile(request):
    # If Admin logs in, show zero registrations to keep student lists pure
    if request.user.is_staff or request.user.is_superuser:
        user_registrations = Registration.objects.none() 
    else:
        user_registrations = Registration.objects.filter(user=request.user).order_by('-registered_at')
    
    return render(request, 'profile.html', {'registrations': user_registrations})

# --- Event Logic ---
@login_required(login_url='student_login') 
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    actual_count = Registration.objects.filter(event=event).count()
    
    # Check if this user (student) is already in the database for this event
    is_registered = Registration.objects.filter(user=request.user, event=event).exists()
    
    # Check if the user is an Admin to show "Manage Event" button
    is_admin_user = request.user.is_staff or request.user.is_superuser

    return render(request, 'detail.html', {
        'event': event, 
        'is_registered': is_registered, 
        'actual_count': actual_count,
        'is_admin_user': is_admin_user
    })

@login_required(login_url='student_login')
def register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    # Block Admins from taking up student seats
    if request.user.is_staff or request.user.is_superuser:
        messages.error(request, "Admins cannot register for events as students.")
        return redirect('detail', event_id=event_id)

    if Registration.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, "Already registered!")
        return redirect('detail', event_id=event_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.event, reg.user = event, request.user
            reg.save()
            event.participants += 1
            event.save()
            messages.success(request, "Registered successfully!")
            return redirect('detail', event_id=event_id)
    else:
        form = RegistrationForm(initial={'email': request.user.email})
    return render(request, 'event_register.html', {'form': form, 'event': event})

# --- Admin Views ---
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Only allow staff/superusers to enter the dashboard
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Admins only.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

@login_required(login_url='admin_login')
def admin_dashboard(request):
    # Extra security check
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')
        
    events = Event.objects.all().order_by('-date')
    
    # THE COUNTERS: Total counts for your dashboard cards
    student_count = User.objects.filter(is_student=True).count()
    event_count = Event.objects.count()
    total_registrations = Registration.objects.count()
    
    return render(request, 'events/admin_dashboard.html', {
        'events': events,
        'event_count': event_count,
        'student_count': student_count,
        'total_registrations': total_registrations
    })