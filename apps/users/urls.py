from django.urls import path
from .views import register_view, login_view, logout_view, ProfileView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]