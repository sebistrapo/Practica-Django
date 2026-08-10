from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.db.models import Q

from .models import *

# Create your views here.
def inicio(req):
    logueado = req.session.get("user", False)
    if not logueado:
        return redirect('login')
    else:
        datos = Mascotas.objects.all()
        contexto = {
            "datos": datos
        }
        return render(req, "index.html", contexto)

def login(req):
    logueado = req.session.get('user', False)
    if logueado:
        return redirect('inicio')
        
    if req.method == 'POST':
        u = req.POST.get('usuario')     
        c = req.POST.get('clave')
        try:
            qry = Usuarios.objects.get(user=u, clave=c)
            req.session['user'] = {
                "id_user": qry.id_user,
                "user": qry.user,
                "clave": qry.clave
            }
            return redirect('inicio')
        except Usuarios.DoesNotExist:
            pass
        return render(req, 'login.html')
    else:
        return render(req, 'login.html')


def logout(req):
    try:
        del req.session['user']
        return redirect('login')
    except Exception as e:
        return redirect('inicio')

def eliminarM(req, id_mascota):
    try:
        qry = Mascotas.objects.get(id_mascota=id_mascota)
        qry.delete()
        return render(req, 'inicio')
    except Exception as e:
        print(f'Error en al eliminar la Mascota: {e}')

def actualizarM(req):
    try:
        pass
    except Exception as e:
        pass