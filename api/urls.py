from django.urls import path, include
# from .views import PostListAPI, PostDetail, PostCreateAPI
from .views import PostViewSet, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
# print(router.urls)


urlpatterns = [
    path('', include(router.urls)),
    # path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('users/', UserViewSet.as_view({'get': 'list'})),
    # path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}))
    # path('posts/', PostListAPI.as_view(),),
    # path('create/', PostCreateAPI.as_view()),
    # path('posts/<int:pk>/', PostDetail.as_view(),)
]