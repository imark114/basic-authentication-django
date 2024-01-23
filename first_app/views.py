from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Created Successfully')
            form.save()
            return redirect('home')
    form = SignUpForm()
    return render(request,'signup.html',{'form': form, 'type': 'Sign Up' })

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username= name, password=user_pass)
            if user is not None:
                messages.success(request,'Logged In Successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Given informations are incorrect')
                return redirect('signup')

    form = AuthenticationForm()
    return render(request,'signup.html',{'form': form,'type':'Login'})

def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('home')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    form = PasswordChangeForm(request.user)
    return render(request,'signup.html',{'form': form, 'type':'Password Change'})
@login_required
def pass_reset(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    form = SetPasswordForm(request.user)
    return render(request,'signup.html',{'form': form, 'type':'Password Reset'})

