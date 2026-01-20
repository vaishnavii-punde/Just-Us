

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

ALLOWED_USERS = ["Guddya", "guddu"]

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.username in ALLOWED_USERS:
                login(request, user)
                return redirect("home")
            else:
                logout(request)
                messages.error(
                    request,
                    "This space is not meant for everyone 🤍"
                )
        else:
            messages.error(request, "Wrong username or password")

    return render(request, "lovehub/login.html")


@login_required(login_url="login")
def home(request):
    return render(request, "lovehub/home.html")
def about(request):
    return render(request, "lovehub/about.html")

def logout_view(request):
    logout(request)
    return redirect("login")