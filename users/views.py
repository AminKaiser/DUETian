from django.shortcuts import render,redirect
from users.forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from users.decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.

@method_decorator(unauthenticated_user, name='dispatch')
class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	posts = Post.objects.all().filter(author=request.user).order_by('-date_posted')
	total_posts = posts.count()

	context = {

		'u_form': u_form,
		'p_form': p_form,
		'posts': posts,
		'total_posts': total_posts,
	}

	return render(request, 'users/profile.html', context)
