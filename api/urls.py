from django.urls import path 
from .views import PostListAPI, PostDetail

urlpatterns = [
    path('posts/', PostListAPI.as_view(),),
    path('posts/<int:pk>/', PostDetail.as_view(),)
]