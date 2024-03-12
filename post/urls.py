from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='name'), 
    path('storage/<str:titulo>/<str:cuerpo>/<int:autor>/',views.storage   ,name="storage"),
    path('consultar/<int:id>',views.consultar,name="consultar"),
    path('modificar/<int:id>/<str:titulo>/',views.modificar,name="modificar"),
    path('eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('storage_autor/<str:nombre>/<str:correo>/',views.storage_autor   ,name="storage_autor"),
    path('consultas',views.consultas,name="consultas"),

]
