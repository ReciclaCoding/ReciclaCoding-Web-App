from django.shortcuts import render


def codigo(request):
    return render(request, 'Registrar_codigo/codigo.html')