from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=100,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
	last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
	email = forms.EmailField(max_length=150, label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['placeholder'] = 'username'

	class Meta:
		model = User
		fields = ['username', 'first_name','last_name','email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
