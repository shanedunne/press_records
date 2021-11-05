from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'title',
        'author',
        'created_time',
        'content',
    )

admin.site.register(Blog, BlogAdmin)