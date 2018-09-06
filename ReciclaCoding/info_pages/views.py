from django.shortcuts import render


def proceso(request):
    return render(request, 'info_pages/proceso.html')


def materiales(request):
    return render(request, 'info_pages/materiales.html')
