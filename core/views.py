from django.shortcuts import render, HttpResponse
from estudiantes.models import Estudiante

def index(request):
    return render(request, "core/index.html")

def profile(request):
    estudiante = Estudiante.objects.all()
    return render(request, "core/profile.html",
    {'estudiante' :estudiante}
    )

def regpagos(request):
    return render(request, "core/regpagos.html")

def becas(request):
    return render(request, "core/becas.html")