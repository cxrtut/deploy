from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'projects/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'projects/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    projects = Project.objects.filter(developer=request.user)
    return render(request, 'projects/dashboard.html', {'projects': projects})

@login_required
def deploy(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.developer = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'projects/deploy.html', {'form': form})

