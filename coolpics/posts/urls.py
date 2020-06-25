from django.urls import path
from .views import PostView, CreatePostView

app_name = 'posts'

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('create/', CreatePostView.as_view(), name='create_post')

    ]