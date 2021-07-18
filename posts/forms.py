from django.forms import ModelForm,Textarea
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['text']
		widgets = {
			"text":Textarea(attrs={'cols':10,'rows':5})
		}


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name','username','email','password1','password2']