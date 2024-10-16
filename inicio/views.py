from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime 
from django.shortcuts import render
from inicio.models import Auto 

def mi_vista (request): 
    return HttpResponse ("hola soy la vista")

def inicio (request):
    #return HttpResponse ("<h1> soy la pantalla de inicio <h1>")
    return render (request, "index.html")

def vista_datos1 (request, nombre):
    nombre_mayuscula = nombre.upper ()
    return HttpResponse (f"hola {nombre_mayuscula}")

def primer_template (request):
    #con with 
    with open (r"templates\primer_template.html") as archivo_del_template:
        template = Template (archivo_del_template.read())

        contexto = Context()

        render_template = template.render (contexto)

        return HttpResponse (render_template)
    


def segundo_template (request):

    fecha_actual = datetime.now()
    datos = {"fecha_actual" : fecha_actual,
    "numeros" : list (range(1,11))
    }

    #v1
    #with open (r"templates\segundo_template.html") as archivo_del_template:
    #   template = Template (archivo_del_template.read())

    #   contexto = Context(datos)

    #  render_template = template.render (contexto)
   
    
    #v2

    #Template = loader.get_template ("segundo_template.html")
    #render_template =Template.render(datos)

    #return HttpResponse (render_template) 
     
    #v3

    return render (request, "segundo_template.html", datos)
    
     
def crear_auto (request, marca, modelo, año):

    auto = Auto (modelo = modelo, marca = marca , año = año) 
    auto.save()
    return render (request, "creacion_auto_correcta.html",{ "auto" : auto}) 