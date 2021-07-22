from django.urls import path
from . import views

urlpatterns = [
    path('', views.pago, name="pago"),
    path('ordenpag/', views.ordenpag, name="ordenpag"),
]