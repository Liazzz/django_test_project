from django.urls import *

from .class_views import (PostsListView, PostDetailsView, UpdatePostView, AddPostView, DeletePostView)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('add/', AddPostView.as_view(), name='add-post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
]
