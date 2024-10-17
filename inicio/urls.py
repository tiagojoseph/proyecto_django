from django.urls import path
from inicio.views import mi_vista, vista_datos1, primer_template, segundo_template, crear_auto, inicio

app_name = "inicio"
urlpatterns = [
         
    path ("mi-vista/", mi_vista, name ="mi_vista"),
    path ("", inicio, name= "inicio"),
    path ("vista-datos/<nombre>", vista_datos1, name= "vista_datos"),
    path ("primer-template/", primer_template, name="primer_template"),
    path ("segundo-template/", segundo_template, name= "segundo_template"),
    path ("crear-auto/<marca>/<modelo>/<año>/", crear_auto, name= "crear_auto"),
    ]