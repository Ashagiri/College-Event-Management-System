from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from events import views 

urlpatterns = [
    # FIXED: Standard path to fix 'AdminSite' error
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.detail, name='detail'),
    path('event/<int:event_id>/register/', views.register, name='register'),
    path('signup/', views.student_signup, name='signup'),
    path('login/student/', views.student_login, name='student_login'),
    
    # FIXED: Added profile back to fix AttributeError
    path('profile/', views.profile, name='profile'),
    
    path('login/admin/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # FIXED: Added this to stop the 'NoReverseMatch' error
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)