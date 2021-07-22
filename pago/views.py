from django.shortcuts import render
from estudiantes.models import Estudiante

def pago(request):
    return render(request, "pago/pago.html")

def ordenpag(request):
    estudiante = Estudiante.objects.all()
    return render(request, "pago/ordenpag.html",
    {'estudiante' :estudiante}
    )