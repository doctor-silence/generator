from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def info(request):
    return render(request, 'generator/info.html')

def password(request):

    characters = list('abcdefghijklmnopqstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQSTUVWXYZ'))
    if request.GET.get('special'):
            characters.extend(list('!@#$%^&*(){}"|:><?'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})