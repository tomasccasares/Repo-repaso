from django.contrib import admin
from django.urls import path
from app_c18.views import (
    data_Curso, data_Entregable,
    data_Estudiante, data_Profesor 
)

urlpatterns = [
    path('Data-Curso/', data_Curso),
    path('Data-Entregable/', data_Entregable),
    path('Data-Estudiante/', data_Estudiante),
    path('Data-Profesor/', data_Profesor),    
]