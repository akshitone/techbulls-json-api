from django.urls import path
from .views import (home, customer_list, customer_create)

urlpatterns = [
    path('', home, name="home"),
    path('customers/', customer_list, name="customers"),
    path('customer-create/', customer_create, name="customer-create"),
]
