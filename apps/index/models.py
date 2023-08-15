from django.db import models

# Create your models here.

class Inventory(models.Model):
    inventory_date = models.DateField()
    gln_client = models.IntegerField()
    gln_branch = models.IntegerField()
    gtin_product = models.IntegerField()
    final_inventory = models.IntegerField()
    unit_price = models.FloatField()
    
    