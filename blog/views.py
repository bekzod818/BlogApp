from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import AddPostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.published.all()
    cats = Category.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'posts': posts, 'cats': cats})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month, publish__day=day)
    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.author = request.user
        new_comment.save()
    else:
        form = CommentForm()
    
    comments = Comment.objects.filter(post=post).order_by('-created')

    return render(request, 'blog/detail.html', {'post': post, 'form': form, 'comments': comments})


def category(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    cat = Category.objects.get(slug=slug)
    cats = Category.objects.all()
    return render(request, 'blog/category.html', {'posts': posts, 'cat': cat, 'cats': cats})


@login_required(login_url='login')
def add_post(request):
    form = AddPostForm()
    if request.method == 'POST':
        # print(request.POST)
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('post_list')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpost.html', {'form': form})


@login_required(login_url='login')
def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = AddPostForm(instance=post)

    if request.user != post.author:
        return HttpResponse("Siz buni o'zgartira olmaysiz")

    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'blog/editpost.html', {'form': form})


@login_required(login_url='login')
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.user != post.author:
        return HttpResponse("Siz buni o'chira olmaysiz")
    else:
        post.delete()
        return redirect('post_list')


def search_post(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    )
    if posts:
        return render(request, 'blog/search.html', {'posts': posts})
    else:
        return redirect('post_list')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        return render(request, 'blog/register.html', {'form': form})  


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('post_list')
        return render(request, 'blog/login.html')


def logoutUser(request):
    logout(request)
    return redirect('post_list')