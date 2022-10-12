from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('service/<str:pk>/', views.service, name='service'),
]