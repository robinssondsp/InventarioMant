# views.py actualizado para reflejar correctamente el path absoluto y detectar imágenes

import os
import pandas as pd
from django.shortcuts import render
from django.conf import settings

EXCEL_PATH = os.path.join(settings.BASE_DIR, 'Inventario.xlsx')

# Ruta correcta absoluta a la carpeta 'herramientas' dentro de static
IMAGENES_PATH = os.path.join(settings.BASE_DIR, 'Trimantapp', 'static', 'herramientas')

def inventario_view(request):
    datos = []
    try:
        df = pd.read_excel(EXCEL_PATH)

        for _, row in df.iterrows():
            sku = str(row.get('SKU', '')).strip()
            herramientas = str(row.get('HERRAMIENTAS', '')).strip()
            cantidades = row.get('CANTIDADES', '')

            imagen_filename = f"{sku}.png"
            imagen_absoluta = os.path.join(IMAGENES_PATH, imagen_filename)
            imagen_existe = os.path.exists(imagen_absoluta)

            datos.append({
                'SKU': sku,
                'HERRAMIENTAS': herramientas,
                'CANTIDADES': cantidades,
                'TIENE_IMAGEN': imagen_existe
            })
    except Exception as e:
        print("[ERROR] Al leer el Excel o procesar imágenes:", e)

    return render(request, 'Trimantapp/inventario.html', {'datos': datos})
