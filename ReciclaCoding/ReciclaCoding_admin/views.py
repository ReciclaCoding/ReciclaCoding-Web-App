from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Hola! Estás en la página de inicio de ReciclaCoding")
