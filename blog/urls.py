from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    path('add/', views.add_blog, name='add_blog'),

]
