# staff/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'staff'
urlpatterns = [
    path('itemrequest/', views.itemrequest, name='itemrequest'),
    path('success/', views.success_view, name='success'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('update_request_status/<int:item_id>/', views.update_request_status, name='update_request_status'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='staff:login'), name='logout'),
    path('delete_reviewed/', views.delete_reviewed_items, name='delete_reviewed_items'),
    path('delete_staff_reviewed/', views.delete_staff_reviewed_items, name='delete_staff_reviewed_items'),  # New URL
]