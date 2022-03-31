from django.urls import path
from .views import post_list, post_detail, add_post, edit_post, delete_post

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name="post_detail"),
    path('addpost/', add_post, name="add_post"),
    path('editpost/<int:post_id>/', edit_post, name='editpost'),
    path('deletepost/<int:post_id>/', delete_post, name="deletepost"),
]