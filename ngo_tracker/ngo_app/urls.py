from django.urls import path, include
urlpatterns = [
    path('ngo_dashboard/', include('ngo_dashboard.urls')),  # NGO dashboard app
]