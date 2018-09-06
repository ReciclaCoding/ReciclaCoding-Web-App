from django.urls import path
from info_pages import views

app_name = 'ReciclaCoding_admin'
urlpatterns = [
    path('proceso', views.proceso, name='Proceso'),
    path('materiales', views.materiales, name='Materiales'),
]