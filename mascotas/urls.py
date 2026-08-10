# URLs de zajuna

from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('eliminarM/', views.eliminarM, name="eliminarM"),
    path('actualizarM/', views.actualizarM, name="actualizarM"),

]