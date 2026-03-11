from django.shortcuts import render, redirect
from django.views import View

from mi_aplicacion.models import Escuela, Alumno, Maestro

from mi_aplicacion.forms import EscuelaForm, MaestroForm

# Create your views here.

class Home(View):
    def get(self, request):
        cdx = {
            "titulo" : "Home",
            "subtitulo" : "Bienvenido a mi aplicación"
        }
        return render(request, 'home/home.html', cdx)
    
class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx = {
            "titulo" : "Escuelas",
            "subtitulo" : "Listado de escuelas",
            "escuelas" : escuelas
        }
        return render(request, 'escuelas/escuelas.html', cdx)
    

class EscuelaAlta(View):
    def get(self, request):
        form = EscuelaForm()
        cdx = {
            "titulo" : "Alta Escuelas",
            "subtitulo": "Alta Escuela",
            "form" : form
        }
        return render(request, 'escuelas/CRUD.html', cdx)

    def post(self, request):
        form = EscuelaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        else:
            cdx = {
                "titulo" : "Alta Escuelas",
                "form" : form,
                "mensaje" : "Error al crear la escuela"
            }
        return render(request, 'escuelas/CRUD.html', cdx)
    
class EscuelaEditar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id = id).first()
        form = EscuelaForm(instance=escuela)
        cdx = {
            "titulo" : "Editar Escuela",
            "subtitulo": "Editar Escuela",
            "form" : form
        }
        return render(request, 'escuelas/CRUD.html', cdx)

    def post(self, request, id):
        escuela = Escuela.objects.filter(id = id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        else:
            cdx = {
                "titulo" : "Editar Escuelas",
                "form" : form,
                "mensaje" : "Error al crear la escuela"
            }
        return render(request, 'escuelas/CRUD.html', cdx)

class EscuelaEliminar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id = id).first()
        form = EscuelaForm(instance=escuela)
        cdx = {
            "titulo" : "Editar Escuela",
            "subtitulo": "Baja Escuela",
            "form" : form
        }
        return render(request, 'escuelas/CRUD.html', cdx)

    def post(self, request, id):
        escuela = Escuela.objects.filter(id = id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        
        return redirect('home')


class Maestros(View):
    def get(self, request):
        maestros = Maestro.objects.all()
        cdx = {
            "titulo" : "Maestros",
            "subtitulo" : "Listado de maestros",
            "maestros" : maestros
        }
        return render(request, 'maestros/maestros.html', cdx)

class MaestroAlta(View):
    def get(self, request):
        form = MaestroForm()
        cdx = {
            "titulo" : "Alta Maestros",
            "subtitulo": "Alta Maestro",
            "form" : form
        }
        return render(request, 'maestros/CRUD.html', cdx)

    def post(self, request):
        form = MaestroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect('home')
    
class MaestroEditar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id = id).first()
        form = MaestroForm(instance=maestro)
        cdx = {
            "titulo" : "Editar Maestro",
            "subtitulo": "Editar Maestro",
            "form" : form
        }
        return render(request, 'maestros/CRUD.html', cdx)

    def post(self, request, id):
        maestro = Maestro.objects.filter(id = id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect('home')

class MaestroEliminar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id = id).first()
        form = MaestroForm(instance=maestro)
        cdx = {
            "titulo" : "Editar Maestro",
            "subtitulo": "Baja Maestro",
            "form" : form
        }
        return render(request, 'maestros/CRUD.html', cdx)

    def post(self, request, id):
        maestro = Maestro.objects.filter(id = id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            maestro.delete()
            return redirect('maestros')
        
        return redirect('home')


    


