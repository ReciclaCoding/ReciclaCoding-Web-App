from django.urls import path
from . import views

app_name = 'ReciclaCoding_admin'
urlpatterns = [
    path('', views.inicio, name='Página de Inicio'),
    path('notes/<int:note_id>/', views.note, name='Nota'),
    path('<mistaken>', views.error, name='Error')
]
