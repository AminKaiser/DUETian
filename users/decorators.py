from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			messages.info(request, f'You are Logged in')
			return redirect('index')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func
