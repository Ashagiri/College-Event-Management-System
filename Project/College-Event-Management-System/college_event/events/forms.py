from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Registration

User = get_user_model()

# ==========================================
# 1. STUDENT SIGNUP FORM (This was missing!)
# ==========================================
class StudentSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email') # Add 'first_name', 'last_name' if needed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True  # Automatically mark as student
        if commit:
            user.save()
        return user

# ==========================================
# 2. REGISTRATION FORM (Existing)
# ==========================================
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone_number']
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        }