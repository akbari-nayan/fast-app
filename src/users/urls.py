from django.urls import path
from .views import UserCreateView,LoginView,HomeView,LogoutView

app_name = 'users'

urlpatterns = [
    path('accounts/register/',UserCreateView.as_view(),name='register-view'),
    path('accounts/login/',LoginView.as_view(),name='login-view'),
    path('accounts/logout/',LogoutView.as_view(),name='logout-view'),
    path('',HomeView.as_view(),name='home-view'),
]