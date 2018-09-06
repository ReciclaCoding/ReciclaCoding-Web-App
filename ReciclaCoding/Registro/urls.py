from django.urls import path
from Registro import views

app_name = 'Registro'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
