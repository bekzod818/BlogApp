from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from blog.models import Post
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


class PostListAPI(ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )


class PostCreateAPI(CreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser, ]


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )