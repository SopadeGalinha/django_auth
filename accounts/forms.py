# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
		
		# Adicione os rótulos (labels)
		labels = {
			'username': 'Create your username',
			'password1': 'Create your password',
			'password2': 'Password confirmation',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text = None
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None
