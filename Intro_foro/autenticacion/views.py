
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "autenticacion/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fsname = request.POST['fsname']
        lsname = request.POST['lsname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username,email,password1)
        myuser_first_name = fsname
        myuser_last_name = lsname

        myuser.save()

        messages.success(request,"Su sesión ha sido creada con éxito.")
        return redirect("signin")

    return render(request, "autenticacion/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fsname = user.first_name
            return render(request, "autenticacion/index.html", {'fsname': fsname})
        else:
            messages(request, "Usuario o contraseña incorrecta")
            return redirect("home")


    return render(request, "autenticacion/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Se ha cerrado sesión de manera exitosa.")
    return redirect("home")
    #olatilines