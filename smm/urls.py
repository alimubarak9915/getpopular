from django.urls import path
from smm import views

app_name = 'smm'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('orders/', views.orders, name='orders'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('services_query/', views.ajax_services_query, name='ajax_services_query'),
    path('service_info/', views.ajax_service_info, name='ajax_service_info'),
    path('create_order/', views.create_order, name='create_order'),
    path('terms-conditions/', views.terms_conditions, name='terms-conditions'),
]
