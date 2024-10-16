from django.urls import path
from inicio.views import mi_vista, inicio, vista_datos1, primer_template, segundo_template, crear_auto

urlpatterns = [
         
    path ("mi-vista/", mi_vista),
    path ("", inicio),
    path ("vista-datos/<nombre>", vista_datos1),
    path ("primer-template/", primer_template),
    path ("segundo-template/", segundo_template),
    path ("crear-auto/<marca>/<modelo>/<año>/", crear_auto)
    ]