from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .tasks import adding_csv
from rest_framework.response import Response
from rest_framework import generics
import csv

# Create your views here.

class InventoryListCreateView(APIView):
    
    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        if csv_file:
            batch_size = 1000  # Tamaño del lote
            data = []
            
        with csv_file.open() as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data.append({
                        "FechaInventario": row["FechaInventario"],
                        "GLN_Cliente": row["GLN_Cliente"],
                        "GLN_sucursal": row["GLN_sucursal"],
                        "Gtin_Producto": row["Gtin_Producto"],
                        "Inventario_Final": int(row["Inventario_Final"]),
                        "PrecioUnidad": float(row["PrecioUnidad"]),
                    })
                    if len(data) >= batch_size:
                        adding_csv.delay(data)  # Envía el lote para su procesamiento
                        data = []  # Reinicia la lista para el próximo lote

            # Procesa el último lote si es necesario
        if data:
            adding_csv.delay(data)
            return Response({"message": "Carga iniciada asincrónicamente."})

        return Response({"message": "No se proporcionó un archivo CSV."})
       
    
    
class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventarioSerializer