from django.urls import path
from . import views

urlpatterns = [
    path('datos/', views.parametros, name='parametros'),
    path('nosotros/', views.nosotros, name='Nosotros'),
    path('formulario/', views.formulario, name='Formulario'),
    path('formulario/datos/', views.parametros, name='parametros'),
    
]
