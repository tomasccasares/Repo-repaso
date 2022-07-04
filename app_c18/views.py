from django.shortcuts import render
from app_c18.models import (
    Curso, Estudiante, Entregable,
    Profesor
)

def data_Curso(request):
    
    contextoCurso = {}
    contextoCurso['curso'] = Curso.objects.all()
    return render(request, 'app_c18/index.html', contextoCurso)    

def data_Estudiante(request):
    
    contextoEstudiante = {} 
    contextoEstudiante['estudiante'] = Estudiante.objects.all()
    return render(request, 'app_c18/index.html', contextoEstudiante)

def data_Entregable(request):
    
    contextoEntregable = {}
    contextoEntregable['entregable'] = Entregable.objects.all()
    return render(request, 'app_c18/index.html', contextoEntregable)

def data_Profesor(request):
    
    contextoProfesor = {}
    contextoProfesor['profesor'] = Profesor.objects.all()
    return render(request, 'app_c18/index.html', contextoProfesor)





