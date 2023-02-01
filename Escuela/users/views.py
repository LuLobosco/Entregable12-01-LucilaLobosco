
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
#from django.views.generic import ListView, CreateView,DeleteView

from users.forms import RegisterForm,UserUpdateForm,UserProfileForm
from users.models import UserProfile

def login_view (request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render (request,'users/login.html', context = context )
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)

            if user is not None:
                login(request, user)
                context = {

                    'message': f'Bienvenido {username}!'
                }
                return render (request, 'index.html',context = context)
        form = AuthenticationForm()

        context = {
            'form': form,
            'errors': 'Usuario o contraseña incorrectos'

            }
        return render(request,'users/login.html',context=context)

def register (request):

    if request.method == 'GET':
        form = RegisterForm()
        context = {

            'form': form
        }
        return render (request,'users/signup.html',context = context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user= user)
            return redirect('login')
        context = {
            'errors': form.errors,
            'form': RegisterForm()
        }
        return render (request,'users/signup.html',context = context)

@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm (
            initial= {
            'username': user.username,
            'first_name': user.first_name
            }
        )
        context = {

            'form': form
        }
        return render (request,'users/update_user.html',context = context)

    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.save()
            return redirect('index')
        context = {
            'errors': form.errors,
            'form': UserUpdateForm()
        }
        return render (request,'users/update_user.html',context = context)

def update_user_profile (request):
    if request.method == 'GET':
        form = UserProfileForm( initial={
        'user': request.user.profile.user,
        'description': request.user.profile.description,
        'link': request.user.profile.link,
        'email': request.user.profile.email,
        'profile_picture' : request.user.profile.profile_picture
            })
        context = {

            'form': form
        }
        return render (request,'users/update_user_profile.html',context = context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.description = form.cleaned_data.get('description')
            request.user.profile.link = form.cleaned_data.get('link')
            request.user.profile.email = form.cleaned_data.get('email')
            request.user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            request.user.profile.save()
            return redirect('index')
        context = {
            'errors': form.errors,
            'form': UserProfileForm()
        }
        return render (request,'users/update_user_profile.html',context = context)

def list_profile(request):

    if 'search' in request.GET:
        search = request.GET['search']
        user = UserProfile.objects.filter(name__contains = search)
    else:
        user = UserProfile.objects.all()
    context = {
        'user': user,
    }
    return render(request,'users/list_profile.html', context = context )