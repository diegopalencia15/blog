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

def consultas(request):
  #obtener todos los elementos de los post
  posts = Post.objects.all()
  #filtrar la consulta por una condicion
  filtro = Post.objects.filter(titulo='adso')
  #filtrar unico resultado
  post = Post.objects.get(id='3')
  #limite de resultados

  limite = Post.objects.all()[:20]
  #del 2 al 4
  limite2 = Post.objects.all()[2:4]
  #ordenar por
  ordenar = Post.objects.all().order_by('cuerpo')
  #obtener menor o igual que 20
  menor = Post.objects.filter(id__lte=20)

  return render(request, 'index.html',{
    'posts':posts, 
    'filtro':filtro,
    'post':post,
    'limite':limite,
    'limite2':limite2,
    'ordenar':ordenar,
    'menor':menor
    })
  #return HttpResponse ("consultas")
