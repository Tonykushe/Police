from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from accounts.forms import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
from django.urls import reverse



# Create your views here.
def home(request):
        return render(request, 'accounts/home.html')



def login_view(request): 
        if request.method == 'POST':
                form = AuthenticationForm(data = request.POST)
                if form.is_valid():
                        # Log user in
                        user = form.get_user()
                        login(request, user)
                        if 'next' in request.POST:
                                return redirect(request.POST.get('next'))
                        else:
                                return redirect('accounts:home')
        else:
                form = AuthenticationForm()
        return render(request, 'accounts/login.html', { 'form' : form })

def signup(request):
	if request.method =='POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = SignupForm()
	return render(request, 'accounts/signup.html', {'form': form})


def view_profile(request):
        args = {'user': request.user}
        return render(request, 'accounts/profile.html', args)

def edit_profile(request):
        if request.method == 'POST':
                form = EditProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                        form.save()
                        return redirect('/accounts/profile')
        else:
                form = EditProfileForm(instance=request.user)
                return render(request, 'accounts/editprofile.html', {'form': form})

def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('social:profile'))

		else:
			return redirect(reverse('social:change-password'))


	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form' : form}
		return render(request, 'accounts/editpassword.html', args)