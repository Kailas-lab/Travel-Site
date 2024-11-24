# travel_package/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('packages/',  views.travel_package_list, name='travel-package-list'),
    path('packages/<int:pk>/',  views.travel_package_detail, name='travel-package-detail'),
    path('bookings/',  views.booking_create, name='booking-create'),

    path('', views.package_list, name='package_list'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
    #path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('confirmation/<int:pk>/', views.booking_confirmation, name='booking_confirmation'),
]
