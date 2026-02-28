from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, Registration, User, College # All models imported here

# 1. COLLEGE ADMIN (This makes NCIT appear!)
admin.site.register(College)

# 2. EVENT ADMIN 
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'participants', 'college') # Added college to list
    search_fields = ('name', 'description', 'location')
    list_filter = ('date', 'college') # You can now filter by college!

admin.site.register(Event, EventAdmin)

# 3. REGISTRATION ADMIN
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'full_name', 'registered_at')
    list_filter = ('event', 'registered_at')
    search_fields = ('user__username', 'event__name', 'email')

admin.site.register(Registration, RegistrationAdmin)

# 4. CUSTOM USER ADMIN
class CustomUserAdmin(UserAdmin):
    model = User
    # This adds your custom fields (department, college, etc.) to the edit page
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('department', 'college', 'is_student', 'is_admin')}),
    )
    list_display = ['username', 'email', 'department', 'college', 'is_staff']

admin.site.register(User, CustomUserAdmin)