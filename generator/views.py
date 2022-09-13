from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ''
    current = list('qwertyuiopasdfghjklzxcvbnm')
    S = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    n = list('0123456789')
    if request.GET.get('capital') == 'on':
        current += S
    if request.GET.get('numbers') == 'on':
        current += n
        
    for i in range(int(request.GET.get('length'))):
        password += random.choice(current)
    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html')