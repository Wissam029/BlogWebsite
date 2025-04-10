from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user/<int:id>/', views.user_posts, name='user_posts'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('blog/<int:id>/', views.blogdetails, name='blogdetails'),
    path('category/<int:id>/', views.posts_by_category, name='posts_by_category'),  # ✅ هذا السطر هو المهم
]
