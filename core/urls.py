from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('perfil/', views.profile, name="profile"),
    path('regpagos/', views.regpagos, name="regpagos"),
    path('becas/', views.becas, name="becas"),
]