from django.urls import path 
from .views import PostListAPI, PostDetail, PostCreateAPI

urlpatterns = [
    path('posts/', PostListAPI.as_view(),),
    path('create/', PostCreateAPI.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view(),)
]