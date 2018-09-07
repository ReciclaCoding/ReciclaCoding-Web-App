from django.urls import path
from Registro import views

app_name = 'Registro'
urlpatterns = [
    path('signup/', views.signup, name='SignUp'),
]
