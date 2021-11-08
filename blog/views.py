from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


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


@login_required
def add_blog(request):
    """ Add a post to the blog section """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorised accounts can create blogs')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Successfully added a blog post!')
            return redirect(reverse('blog_post', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog post. Please ensure the form is valid.')
    else:
        form = BlogForm()
        
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorised users can edit blogs')
        return redirect(reverse('home'))
    
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog_post', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorised users can delete blogs.')
        return redirect(reverse('all_blogs'))
    
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('all_blogs'))

