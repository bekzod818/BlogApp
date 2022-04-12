from django.urls import path
from .views import post_list, post_detail, add_post, edit_post, delete_post, search_post, registerUser, loginUser, logoutUser, category, ContactView

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name="post_detail"),
    path('addpost/', add_post, name="add_post"),
    path('editpost/<int:post_id>/', edit_post, name='editpost'),
    path('deletepost/<int:post_id>/', delete_post, name="deletepost"),
    path('search/', search_post, name="search"),
    path('register/', registerUser, name="register"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('category/<slug:slug>/', category, name="category"),
    path('contact/', ContactView.as_view(), name="contact"),
]