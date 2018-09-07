from django.urls import path
from Formulario import views

app_name = 'Formulario'
urlpatterns = [
    path('formulario/', views.formulario, name='Formulario'),
]
