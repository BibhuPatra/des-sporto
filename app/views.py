from django.shortcuts import render
from .models import Players
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def index(request):

    return render(request,"index.html")

def signup(request):

    return render(request,"Regi.html")

def signup_action(request):

    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    players = Players(player_name=name,email=email,password=password)
    players.save()
    messages.info(request, 'You have signed up successfully !!!')
    return HttpResponseRedirect(reverse("signup"))