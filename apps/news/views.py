from django.shortcuts import render, redirect
# from apps.customuser.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'news/home.html')

