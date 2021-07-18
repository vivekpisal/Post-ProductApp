from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm,RegisterForm
from django.contrib.auth.models import User


@login_required(login_url="/login/")
def allposts(request):
	template_name = 'main/posts.html'
	postform = PostForm()
	posts = Post.objects.filter(user=request.user)
	context={'posts':posts,'postform':postform,"allposts":"active"}
	return render(request,template_name,context)


@login_required(login_url="/login/")
def addpost(request):
	if request.method == 'POST':
		postform = PostForm(request.POST)
		post = postform.save(commit=False)
		post.user = request.user 
		post.save()
		return redirect(allposts)


@login_required(login_url="/login/")
def delete_post(request,id):
	if id:
		post = Post.objects.get(id=id)
		post.delete()
		return redirect(allposts)


def register(request):
	if request.method == "POST":
		user = RegisterForm(request.POST)
		user.save()
		return redirect("/")
	else:
		registerform = RegisterForm()
		context = {"registerform":registerform,"register":"active"}
		return render(request,"main/register.html",context)


@login_required(login_url="/login/")
def userinfo(request):
	template_name = 'main/userinfo.html'
	user = User.objects.get(username=request.user)
	context = {"user":user,"userinfo":"active"}
	return render(request,template_name,context)


@login_required(login_url="/login")
def editpost(request,id):
	template_name = 'main/editpost.html'
	post_object = Post.objects.get(id=id)
	if request.method == "GET":
		post = Post.objects.get(id=id)
		form = PostForm(instance=post)
		context = {"form":form,"editpost":"active"}
		return render(request,template_name,context)
	else:
		post_object.text = request.POST['text']
		post_object.save()
		return redirect(allposts)