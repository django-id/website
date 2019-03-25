from django.test import TestCase

from app_forum.models import Forum, Comment


class ForumModelTestCase(TestCase):

    def test_forum_model_str_method(self):
        forum = Forum(forum_title='Example')
        self.assertEqual(str(forum), 'Example')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Forum._meta.verbose_name_plural), u'Title')

    def test_comment_model_str_method(self):
        comment = Comment(comment_content='Good!')
        self.assertEqual(str(comment), 'Good!')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Comment._meta.verbose_name_plural), u'Comment')
