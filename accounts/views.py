from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import *
from django.contrib.auth import login, logout

# Create your views here.
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
                                return redirect('articles:list')
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

		args = {'form': form}
		return render(request, 'accounts/signup.html', args)
 