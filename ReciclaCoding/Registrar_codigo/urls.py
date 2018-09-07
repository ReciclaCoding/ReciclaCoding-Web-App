from django.urls import path
from Registrar_codigo import views

app_name = 'Registrar_codigo'
urlpatterns = [
    path('codigo/', views.codigo, name='Registrar_codigo'),
]
