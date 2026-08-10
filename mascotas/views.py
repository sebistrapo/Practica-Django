from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.db.models import Q

from .models import *
from .utils import *

# Create your views here.
def inicio(req):
    logueado = req.session.get("user", False)
    if not logueado:
        return redirect("login")
    else:
        datos = Mascotas.objects.all()
        contexto = {
            "datos": datos
        }
        return render(req, "index.html", contexto)