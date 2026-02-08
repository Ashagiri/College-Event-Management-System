from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, Registration, User

# 1. EVENT ADMIN (Your existing code)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'participants')
    search_fields = ('name', 'description', 'location')
    list_filter = ('date',)

admin.site.register(Event, EventAdmin)

# 2. REGISTRATION ADMIN (New)
# This lets you see a list of who signed up for what
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'full_name', 'registered_at')
    list_filter = ('event', 'registered_at') # Filter by Event
    search_fields = ('user__username', 'event__name', 'email')

admin.site.register(Registration, RegistrationAdmin)

# 3. CUSTOM USER ADMIN (Crucial!)
# This lets you see/edit the 'is_student' and 'is_admin' flags
class CustomUserAdmin(UserAdmin):
    model = User
    # This adds your custom flags to the user edit page in Admin
    fieldsets = UserAdmin.fieldsets + (
        ('User Roles', {'fields': ('is_student', 'is_admin')}),
    )
    # Shows these columns in the user list
    list_display = ['username', 'email', 'is_student', 'is_admin', 'is_staff']

admin.site.register(User, CustomUserAdmin)