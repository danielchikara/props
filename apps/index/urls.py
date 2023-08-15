from django.urls import path
from .views import *

app_name = 'index'
urlpatterns = [
    path('api/inventory/', InventoryListCreateView.as_view(), name='inventory_create'),
    path('api/inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
   
    

]