from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import CreatePostForm
# Create your views here.


class PostView(ListView):
    model = Post
    template_name = 'posts.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'createpost.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:post')