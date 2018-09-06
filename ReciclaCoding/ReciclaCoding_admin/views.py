from django.shortcuts import render, get_object_or_404
from django.http import Http404
from ReciclaCoding_admin.models import Note, Register1, Register2


def inicio(request):
    notes_list = Note.objects.order_by('-publish_date')[:3]
    context = {'notes_list': notes_list}
    return render(request, 'ReciclaCoding_admin/inicio.html', context)


def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'ReciclaCoding_admin/notas.html', {'note': note})


def recycle(request):
    recycle_list = Register1.objects.order_by('register_recycle')
    context = {'recycle_list': recycle_list}
    return render(request, 'ReciclaCoding_admin/recicladoras.html', context)


def r_names(request, recycle_id):
    recycle = get_object_or_404(Register1, pk=recycle_id)
    r_workers = Register2.objects.filter(recycle_id=recycle_id)
    context = {'recycle': recycle, 'r_workers': r_workers}
    return render(request, 'ReciclaCoding_admin/recicladora.html', context)
