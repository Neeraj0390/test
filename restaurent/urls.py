from django.contrib import admin
from django.urls import path, include
from staff.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),  # Set login as the landing page
    path('staff/', include('staff.urls')),  # Include staff app URLs under /staff/
]
