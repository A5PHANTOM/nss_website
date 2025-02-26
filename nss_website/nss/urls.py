from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from . import views
from django.conf import settings
from .views import manage_events, delete_event

urlpatterns = [
    # Home & Admin Routes
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("logout/", LogoutView.as_view(next_page="admin_login"), name="logout"),
    path("volunteers/", views.volunteers, name="volunteers"),

    # Programs Management
    path('programs/', views.programs, name='programs'),  # ✅ List Programs
    path('programs/add/', views.add_program, name='add_program'),  # ✅ Add Program
    path('programs/modify/<int:pk>/', views.modify_program, name='modify_program'),  # ✅ Modify Program
    path('programs/remove/<int:pk>/', views.remove_program, name='remove_program'),  # ✅ Remove Program
    path('programs/view/<int:pk>/', views.view_program, name='view_program'),  # ✅ View Program
    path("programs/photo/delete/<int:photo_id>/", views.delete_program_photo, name="delete_program_photo"),
    path("programs/more_photo/delete/<int:photo_id>/", views.delete_more_program_photo, name="delete_more_program_photo"),
    path("events/", views.events, name="events"),

#path to manage evenrs 
    path('manage-events/', manage_events, name='manage_events'),
    path('delete-event/<int:event_id>/', delete_event, name='delete_event'),

    # Admin Panel URLs (Custom Admin Page)
    path('admin/programs/', views.admin_programs, name='admin_programs'),  # ✅ Custom Admin Page for Programs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
