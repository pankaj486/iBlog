from django import forms
from .models import Category, Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['cat', 'title', 'content', 'url', 'image']


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comments']
