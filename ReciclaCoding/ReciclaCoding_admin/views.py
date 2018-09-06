from django.shortcuts import render, get_object_or_404
from django.http import Http404
from ReciclaCoding_admin.models import Note


def inicio(request):
    notes_list = Note.objects.order_by('-publish_date')[:3]
    context = {'notes_list': notes_list}
    return render(request, 'ReciclaCoding_admin/inicio.html', context)


def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'ReciclaCoding_admin/notas.html', {'note': note})


def error(request, mistaken):
    raise Http404("La página no se ha creado aún")
