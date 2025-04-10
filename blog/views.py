from django.shortcuts import render
from .models import User, Post, Comment, Category
from django.shortcuts import render, get_object_or_404
def main(request):
    users = User.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/main.html', {
        'users': users,
        'categories': categories
    })


def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})


def blogdetails(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/blogdetails.html', {'post': post})
from django.shortcuts import render

def user_posts(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user=user)
    comments = Comment.objects.filter(user=user)
    return render(request, 'blog/user_posts.html', {
        'user': user,
        'posts': posts,
        'comments': comments
    })
def posts_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/posts_by_category.html', {
        'category': category,
        'posts': posts
    })
