from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario_view, name='home'),  # <- Agregamos ruta raíz
    path('inventario/', views.inventario_view, name='inventario'),
]
