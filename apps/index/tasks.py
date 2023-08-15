from celery import shared_task
from .models import Inventory

@shared_task
def adding_csv(data):
    # Procesa los datos del SVG y almacénalos en la base de datos
    # Por ejemplo:
    for item in data:
        Inventory.objects.create(**item)