from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from blog.models import Post
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, mixins, pagination
from django.contrib.auth.models import User


class StandartPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class PostViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)
    # pagination_class = StandartPagination


class UserViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAuthenticated)
    pagination_class = StandartPagination

# class PostListAPI(ListAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthenticated, )


# class PostCreateAPI(CreateAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAdminUser, ]


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Post.published.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthorOrReadOnly, )