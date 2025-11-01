from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ngo_app.urls')),  # Load homepage from ngo_app
    path('users/', include('users.urls')),
    path('ngo_dashboard/', include('ngo_dashboard.urls')),
]