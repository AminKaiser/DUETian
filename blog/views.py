from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView
from blog.models import Post,Comment
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class IndexView(ListView):
	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'posts'
	paginate_by = 3
	ordering = ['-date_posted']

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class JobPostView(ListView):
	model = Post
	template_name = 'blog/job_posts.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self):
		return Post.objects.filter(category='Job Post').order_by('-date_posted')

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
	model = Post
	fields = ['category','title', 'content','picture']
	success_message = "Post was created successfully"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDetailView(DetailView):
	model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin, UpdateView):
	model = Post
	fields = ['category','title', 'content','picture']
	success_message = "Post updated successfully!"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('index')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class CreateComment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Comment
	fields = ['text',]
	success_message = "Comment added!"

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	fields = ['text',]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False


# class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# 	model = Comment
# 	success_url = 'index'
#
# 	def test_func(self):
# 		comment = self.get_object()
# 		if self.request.user == comment.author:
# 			return True
# 		return False

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post-detail', pk=post_pk)
