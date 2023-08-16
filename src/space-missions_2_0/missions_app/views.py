from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import SpaceMission

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if(request.method=="POST"):
        if(request.POST['password1'] == request.POST['password2']):
            try:
                newUser = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                newUser.save()
                login(request, newUser)#crea cookie de la sesion
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': "Username already exist"
                })
        return render(request, 'signup.html', {
            'error': "Password do not match"
        })
    
    else:
        return render(request, 'signup.html')
    
def missions(request):
    spaceMissions = SpaceMission.objects.all()
    return render(request, 'missions.html', {'spaceMissions': spaceMissions})

def createSpaceMission(request):
    if(request.method=="GET"):
        return render(request, 'createMissions.html')
    else:
        try:
            SpaceMission(title = request.POST['title'], description = request.POST['description'], user = request.user).save()
            return redirect('missions')
        except ValueError:
            return render(request, 'createMissions.html', {
                'error': 'Ocurrió un error, ingresa datos válidos'
            })

def contacto(request):
    return render(request, 'html/contacto.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if(request.method == "GET"):
        return render(request, 'signin.html')
    else:
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])

        if(user is None):
            return render(request, 'signin.html', {
                'error': "Username or password incorrect",
            })
        else:
            login(request, user)
            return redirect('home')
