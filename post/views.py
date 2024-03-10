from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Autor

# Create your views here.
def index(request):
  post=Post.objects.all()
  for obj in post:
    print("Title : ",obj.titulo)
  return HttpResponse('lista de posts')

def  storage(request,titulo,cuerpo,autor):
  autor = Autor.objects.get(id=autor)
  print(f'{titulo},{cuerpo},{autor}')
  post = Post(titulo=titulo, cuerpo=cuerpo, autor=autor )
  post.save()
  print(autor)
  return HttpResponse(f'Guardamos los datos{autor}')

def  storage_autor(request,nombre,correo):
  post = Autor(nombre=nombre, correo=correo )
  post.save()
  print(correo)
  return HttpResponse('Guardamos Autor')

def  consultar (request, id):
  post = Post.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (post)
  return HttpResponse (f"Nombre: {post.titulo}, Cuerpo: {post.cuerpo}, fecha: {post.fecha}, autor: {post.autor}")  
  
def  modificar(request,titulo,id):
    
  post = Post.objects.get(id=id)
  post.titulo = titulo
  post.save()

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  post = Post.objects.get(id=id)
  post.delete()
  return HttpResponse ("Registro Eliminado")