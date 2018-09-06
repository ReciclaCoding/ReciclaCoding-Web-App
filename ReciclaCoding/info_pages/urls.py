from django.urls import path
from info_pages import views

app_name = 'info_pages'
urlpatterns = [
    path('proceso', views.proceso, name='Proceso'),
    path('materiales', views.materiales, name='Materiales'),
]