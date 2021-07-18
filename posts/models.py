from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True,editable=True)

	def __str__(self):
		return f"User:- {self.user} Text:- {self.text} Last updated:- {self.updated_at}"

