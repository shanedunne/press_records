from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    """
    A view to show all blogs
    """
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
    }

    return render(request, 'blog/all_blogs.html', context)


def blog_post(request, blog_id):
    """ A view to show single blogs """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)
