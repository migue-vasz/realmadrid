from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Jugador, Partido, Rotacion, Goal
from .forms import FormPartido

def nueva_partido(request):
    if request.method == "POST":
        form = FormPartido(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('detalle_partido', pk=p.pk)
    else:
        form = FormPartido()
    return render(request, 'club/nueva_partido.html', {'formulario': form})

def listar_partidos(request):
    p = Partido.objects.filter(fecha_partido__lte=timezone.now()).order_by('fecha_partido')
    return render(request, 'club/listar_partidos.html', {'p': p})

def detalle_partido(request, pk):
    p = get_object_or_404(Partido, pk=pk)
    return render(request, 'club/detalle_partido.html', {'p': p})

def editar_partido(request, pk):
    p = get_object_or_404(Partido, pk=pk)
    if request.method == "POST":
        form = FormPartido(request.POST, instance=p)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('detalle_partido', pk=p.pk)
    else:
        form = FormPartido(instance=p)
    return render(request, 'club/editar_partido.html', {'formulario': form})

def eliminar_partido(request, pk):
    p = get_object_or_404(Partido, pk=pk)
    p.delete()
    return redirect('listar_partidos')

def publicar_partido(request, pk):
    p = get_object_or_404(Partido, pk=pk)
    p.publicar()
    return redirect('detalle_partido', pk=p.pk)

def listar_borrador(request):
    p = Partido.objects.filter(fecha_partido__isnull=True).order_by('fecha_partido')
    return render(request, 'club/listar_borrador.html', {'p': p})
