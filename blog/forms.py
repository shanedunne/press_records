from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = 'image', 'title', 'content'

    image = forms.ImageField(label='image',
                             required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Blog Title'
        self.fields['content'].widget.attrs['placeholder'] = 'Blog Content'
