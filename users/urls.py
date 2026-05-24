from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, profile, cancel_booking

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
]