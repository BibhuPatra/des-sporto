"""des_sporto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('signup-action/',views.signup_action,name="signup_action"),
    path('search/',views.search,name='search'),
    path('institute/<int:id>/',views.public_profile,name='public_profile'),
    path('search-result/',views.search_result,name='search_result'),
    path('institute/',views.institute,name='institute'),
]
