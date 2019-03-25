from django.test import TestCase
from app_forum.models import Forum, Comment
from app_forum.forms import CommentForm, ThreadForm

# test for forms

class CommentFormTest(TestCase):

    def test_comment_forms(self):
        form_data = {
            'comment_content' : 'comment'
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

class ThreadFormTest(TestCase):

    def test_thread_forms(self):
        thread_data = {
            'forum_title' : 'title',
            'forum_category' : 'category',
            'forum_content' : 'content'
        }
        thread = ThreadForm(data=thread_data)
        self.assertFalse(thread.is_valid())
