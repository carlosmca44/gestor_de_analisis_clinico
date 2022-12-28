from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),

    # Auth system
    path('accounts/login/',
         LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/login.html'), name='logout'),

    # User management
    path('users-management/new/', views.createUser, name='createUser'),
]
