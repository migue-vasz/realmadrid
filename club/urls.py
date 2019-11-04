from django.urls import path
from . import views

urlpatterns = [
    path('game/new', views.nueva_partido, name='nueva_partido'),
    path('', views.listar_partidos, name='listar_partidos'),
    path('game/<int:pk>/', views.detalle_partido, name='detalle_partido'),
    path('game/<int:pk>/editar/', views.editar_partido, name='editar_partido'),
    path('game/<pk>/eliminar/', views.eliminar_partido, name='eliminar_partido'),
    path('borr/', views.listar_borrador, name='listar_borrador'),

#    path('', views.listar_pub, name='listar_pub'),
#    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
#
#    path('pub/<int:pk>/editar/', views.editar_pub, name='editar_pub'),
#    path('bor/', views.listar_bor, name='listar_bor'),
#    path('pub/<pk>/publicar/', views.publicar_pub, name='publicar_pub'),
#    path('pub/<pk>/eliminar/', views.eliminar_pub, name='eliminar_pub'),
]
