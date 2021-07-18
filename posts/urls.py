from django.urls import path
from .views import *

urlpatterns = [
    path('',allposts,name="allposts"),
    path('addpost',addpost,name="addpost"),
    path('delete/<int:id>',delete_post,name="deletepost"),
    path('register',register,name="register"),
    path('userinfo',userinfo,name="userinfo"),
    path('editpost/<int:id>',editpost,name="editpost")
]