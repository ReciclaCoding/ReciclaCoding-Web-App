from django.shortcuts import render


def formulario(request):
    return render(request, 'Formulario/formulario.html')