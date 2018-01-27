from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from accounts.forms import *
from django.contrib.auth import login, logout


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


def profile(request):
        args = {'user': request.user}
        return render(request, 'accounts/profile.html', args)
 