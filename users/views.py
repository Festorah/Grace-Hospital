from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

authentication = 'admin'
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			if form.cleaned_data.get('authentication') == authentication:
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Your account has been created! You are now able to log in')
				return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})



@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form. is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been Updated')
			return redirect('profile')
			
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	name = User.objects.filter(username='funso').first()
	context = {
		'u_form': u_form,
		'p_form': p_form,
		'name': name,
	}

	return render(request, 'users/profile.html', context)