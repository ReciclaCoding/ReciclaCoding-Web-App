from django.urls import path
from ReciclaCoding_admin import views

app_name = 'ReciclaCoding_admin'
urlpatterns = [
    path('', views.inicio, name='Página de Inicio'),
    path('notes/<int:note_id>/', views.note, name='Nota'),
    path('recicladoras/', views.recycle, name='Recicladoras'),
    path('recicladoras/<int:recycle_id>', views.r_names, name='Recicladora'),
]
