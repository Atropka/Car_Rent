from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('cars/', views.cars, name='cars'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),  # Основная форма контакта
    path('contact_sent/', views.contact_sent, name='contact_sent'),  # Успешная отправка
    path('car_list/', views.car_list, name='car_list'),  # Список машин
]
