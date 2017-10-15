from django import forms
from markdownx.fields import MarkdownxFormField

from .models import Forum, Comment


class ThreadForm(forms.ModelForm):
    """
    Comment Form
    """
    class Meta:
        model = Forum
        fields = (
            'forum_title',
            'forum_category',
            'forum_content',
        )
        comment_content = MarkdownxFormField()
        exclude = ['forum_author', 'is_hot']
        widgets = {'forum_author': forms.HiddenInput()}


class CommentForm(forms.ModelForm):
    """
    Comment Form
    """
    class Meta:
        model = Comment
        fields = (
            'comment_content',
        )
        comment_content = MarkdownxFormField()
        exclude = ['comment_author']
        widgets = {'comment_author': forms.HiddenInput()}
