from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', views.login, name='login'),
    path('accounts/auth/', views.auth_view, name='auth'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/loggedin/', views.loggedin, name='loggedin'),
    path('accounts/invalid/', views.invalid_login, name='invalid'),
    path('accounts/register/', views.register_user, name='register'),
    path('accounts/register_success/', views.register_success, name='register_success'),
]
