from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('tinymce/', include('tinymce.urls')),

]
