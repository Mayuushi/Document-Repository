from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('login/', views.login_view, name='login'),
]
