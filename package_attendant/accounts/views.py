from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from accounts.forms import UserRegisterForm, AuthenticationForm, UserCreationForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfile





# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        user = request.POST['username']
        passcode = request.POST['password']
        user = authenticate(request, username=user, password=passcode)
        if user is not None:
            login(request, user)
            return redirect('main/home.html')
        else:
            return render(request, 'registration/login.html')


def LogoutView(request):
    logout(request)
    return redirect('registration/logout.html')
   

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('..')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html',{'form': form})


def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('/profile/')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)

