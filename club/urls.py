from django.urls import path
from . import views

urlpatterns = [
    path('game/new', views.nuevo_partido, name='nuevo_partido'),
    path('', views.listar_partidos, name='listar_partidos'),
    path('game/<int:pk>/editar/', views.editar_partido, name='editar_partido'),
    path('game/<pk>/eliminar/', views.eliminar_partido, name='eliminar_partido'),
    path('game/<int:pk>/', views.detalle_partido, name='detalle_partido'),

    path('rotation/new', views.nueva_rotacion, name='nueva_rotacion'),
    path('rotation/', views.listar_rotaciones, name='listar_rotaciones'),
    path('rotation/<int:pk>/editar/', views.editar_rotacion, name='editar_rotacion'),
    path('rotation/<pk>/eliminar/', views.eliminar_rotacion, name='eliminar_rotacion'),
    path('rotation/<int:pk>/', views.detalle_rotacion, name='detalle_rotacion'),

    path('player/new', views.nuevo_jugador, name='nuevo_jugador'),
    path('player/', views.listar_jugadores, name='listar_jugadores'),
    path('player/<int:pk>/editar/', views.editar_jugador, name='editar_jugador'),
    path('player/<pk>/eliminar/', views.eliminar_jugador, name='eliminar_jugador'),
    path('player/<int:pk>/', views.detalle_jugador, name='detalle_jugador'),

    path('goal/new', views.nuevo_goal, name='nuevo_goal'),
    path('goal/', views.listar_goals, name='listar_goals'),
    path('goal/<int:pk>/editar/', views.editar_goal, name='editar_goal'),
    path('goal/<pk>/eliminar/', views.eliminar_goal, name='eliminar_goal'),
    path('goal/<int:pk>/', views.detalle_goal, name='detalle_goal'),
]
