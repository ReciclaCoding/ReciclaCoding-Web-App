from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    identification = forms.CharField(help_text='Ingrese su # de cédula')
    first_name = forms.CharField(help_text='Ingrese su Nombre')
    last_name = forms.CharField(help_text='Ingrese su Apellido')
    phone = forms.CharField(help_text='Ingrese su número de telefónico')
    location = forms.CharField(help_text='Ingrese la dirección de su domicilio')
    birth_date = forms.CharField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'identification', 'first_name', 'last_name', 'phone', 'location',
                  'birth_date', 'password1', 'password2', )
