from django.shortcuts import render
from .models import Players
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.urls import reverse
from .models import Institute
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
    messages.success(request, 'You have signed up successfully !!!')
    return render(request,'success.html')

def search(request):

    return render(request,'search.html')

def institute(request):

    return render(request,"profile.html")

def search_result(request):
    search = request.GET.get("institute")
    institute = Institute.objects.filter(institute_name__contains=search).values("institute_id","institute_name","contact","location","no_coaches","no_players","category","age_group")
    return render(request,"search_result.html",{"institutes":list(institute)})

def public_profile(request,id):
    institute = Institute.objects.get(institute_id=id)
    return render(request,"public_profile.html",{"institute":institute})
