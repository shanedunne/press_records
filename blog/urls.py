from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    # path('add/', views.add_product, name='add_product'),
    # path('edit<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete<int:product_id>/', views.delete_product, name='delete_product'),

]
