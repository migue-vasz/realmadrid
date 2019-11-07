from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Jugador, Partido, Rotacion, Goal
from .forms import FormPartido, FormJugador, FormRotacion, FormGoal

#Partido
def nuevo_partido(request):
    if request.method == "POST":
        form = FormPartido(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('detalle_partido', pk=p.pk)
    else:
        form = FormPartido()
    return render(request, 'club/nuevo_partido.html', {'formulario': form})

def listar_partidos(request):
    p = Partido.objects.filter(fecha_partido__lte=timezone.now()).order_by('fecha_partido')
    return render(request, 'club/listar_partidos.html', {'p': p})

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

def detalle_partido(request, pk):
    p = get_object_or_404(Partido, pk=pk)
    return render(request, 'club/detalle_partido.html', {'p': p})

#Jugador
def nuevo_jugador(request):
    if request.method == "POST":
        form = FormJugador(request.POST)
        if form.is_valid():
            j = form.save(commit=False)
            j.save()
            return redirect('detalle_jugador', pk=j.pk)
    else:
        form = FormJugador()
    return render(request, 'club/nuevo_jugador.html', {'formulario': form})

def listar_jugadores(request):
    j = Jugador.objects.filter().order_by('dorsal')
    return render(request, 'club/listar_jugadores.html', {'j': j})

def editar_jugador(request, pk):
    j = get_object_or_404(Jugador, pk=pk)
    if request.method == "POST":
        form = FormJugador(request.POST, instance=j)
        if form.is_valid():
            j = form.save(commit=False)
            j.save()
            return redirect('detalle_jugador', pk=j.pk)
    else:
        form = FormJugador(instance=j)
    return render(request, 'club/editar_jugador.html', {'formulario': form})

def eliminar_jugador(request, pk):
    j = get_object_or_404(Jugador, pk=pk)
    j.delete()
    return redirect('listar_jugadores')

def detalle_jugador(request, pk):
    j = get_object_or_404(Jugador, pk=pk)
    return render(request, 'club/detalle_jugador.html', {'j': j})

#Rotacion
def nueva_rotacion(request):
    if request.method == "POST":
        form = FormRotacion(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.save()
            return redirect('detalle_rotacion', pk=r.pk)
    else:
        form = FormRotacion()
    return render(request, 'club/nueva_rotacion.html', {'formulario': form})

def listar_rotaciones(request):
    r = Rotacion.objects.filter().order_by('partido')
    return render(request, 'club/listar_rotaciones.html', {'r': r})

def editar_rotacion(request, pk):
    r = get_object_or_404(Rotacion, pk=pk)
    if request.method == "POST":
        form = FormRotacion(request.POST, instance=r)
        if form.is_valid():
            r = form.save(commit=False)
            r.save()
            return redirect('detalle_rotacion', pk=r.pk)
    else:
        form = FormRotacion(instance=r)
    return render(request, 'club/editar_rotacion.html', {'formulario': form})

def eliminar_rotacion(request, pk):
    r = get_object_or_404(Rotacion, pk=pk)
    r.delete()
    return redirect('listar_rotaciones')

def detalle_rotacion(request, pk):
    r = get_object_or_404(Rotacion, pk=pk)
    return render(request, 'club/detalle_rotacion.html', {'r': r})

#Goal
def nuevo_goal(request):
    if request.method == "POST":
        form = FormGoal(request.POST)
        if form.is_valid():
            g = form.save(commit=False)
            g.save()
            return redirect('detalle_goal', pk=g.pk)
    else:
        form = FormGoal()
    return render(request, 'club/nuevo_goal.html', {'formulario': form})

def listar_goals(request):
    g = Goal.objects.filter().order_by('partido')
    return render(request, 'club/listar_goals.html', {'g': g})

def editar_goal(request, pk):
    g = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        form = FormGoal(request.POST, instance=g)
        if form.is_valid():
            g = form.save(commit=False)
            g.save()
            return redirect('detalle_goal', pk=g.pk)
    else:
        form = FormGoal(instance=g)
    return render(request, 'club/editar_goal.html', {'formulario': form})

def eliminar_goal(request, pk):
    g = get_object_or_404(Goal, pk=pk)
    g.delete()
    return redirect('listar_goals')

def detalle_goal(request, pk):
    g = get_object_or_404(Goal, pk=pk)
    return render(request, 'club/detalle_goal.html', {'g': g})
