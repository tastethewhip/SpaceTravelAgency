from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('trips/', views.all_trips, name='trips'),
    path('trips/<int:product_id>/', views.trip_detail, name='trip_detail'),
]