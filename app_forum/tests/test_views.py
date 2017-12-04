from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from app_forum.models import Category, Forum, Comment
from app_forum.views import (forum_list_view, forum_new_view, forum_single_view,
                             forum_edit_view, forum_comment_edit_view)


class ForumViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_retrieve_forum_list_view(self):
        url = reverse('forum:forum_list')
        request = self.factory.get(path=url)
        response = forum_list_view(request)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_forum_list_view_with_invalid_paging_page(self):
        url = reverse('forum:forum_list')
        url += '?page=A'
        request = self.factory.get(path=url)
        response = forum_list_view(request)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_forum_list_view_with_empty_paging_page(self):
        url = reverse('forum:forum_list')
        url += '?page=90'
        request = self.factory.get(path=url)
        response = forum_list_view(request)
        self.assertEqual(response.status_code, 200)

    def test_create_new_thread_view(self):
        user = User.objects.create_user(
            username='tester',
            email='tester@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        url = reverse('forum:forum_new')
        payload = {
            'forum_title': 'Test new thread',
            'forum_category': category.pk,
            'forum_content': 'Lorep insum dolor amet.',
        }

        request = self.factory.post(path=url, data=payload)
        request.user = user
        response = forum_new_view(request)
        response.client = Client()
        self.assertRedirects(response, reverse('forum:forum_list'))

    def test_retrieve_new_thread_form_view(self):
        user = User.objects.create_user(
            username='tester',
            email='tester@gmail.com',
            password='testing123',
        )
        url = reverse('forum:forum_new')

        request = self.factory.get(path=url)
        request.user = user
        response = forum_new_view(request)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_single_thread(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=user.profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )
        url = reverse('forum:forum_single', args=[forum.pk])
        request = self.factory.get(path=url)
        response = forum_single_view(request, forum.pk)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_single_thread_and_post_a_comment(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=user.profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )

        payload = {
            'comment_content': 'Good post!'
        }
        url = reverse('forum:forum_single', args=[forum.pk])
        request = self.factory.post(path=url, data=payload)
        request.user = user
        response = forum_single_view(request, forum.pk)
        response.client = Client()
        self.assertRedirects(response, reverse('forum:forum_single', args=[forum.pk]))

    def test_forum_edit_view(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=user.profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )

        payload = {
            'forum_title': 'I change my mind to change the title',
            'forum_content': 'Lorep insum dolor amet.',
            'forum_category': category.pk,
        }
        url = reverse('forum:forum_edit', args=[forum.pk])
        request = self.factory.post(path=url, data=payload)
        request.user = user
        response = forum_edit_view(request, forum.pk)
        response.client = Client()
        self.assertRedirects(response, reverse('forum:forum_single', args=[forum.pk]))

    # def test_forum_edit_view_with_different_author(self):
    #     user = User.objects.create_user(
    #         username='john',
    #         email='john.doe@gmail.com',
    #         password='testing123',
    #     )
    #     another_user = User.objects.create_user(
    #         username='jack',
    #         email='jack@gmail.com',
    #         password='testing123',
    #     )
    #     category = Category.objects.create(category_title='Testing')
    #     forum = Forum.objects.create(
    #         forum_author=user.profile,
    #         forum_title='Test new thread.',
    #         forum_category=category,
    #         forum_content='Lorep insum dolor amet.',
    #     )
    #     with self.assertRaises(PermissionDenied):
    #         url = reverse('forum:forum_edit', args=[forum.pk])
    #         request = self.factory.get(path=url)
    #         request.user = another_user
    #         forum_edit_view(request, forum.pk)

    def test_retrieve_forum_edit_form_view(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=user.profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )

        url = reverse('forum:forum_edit', args=[forum.pk])
        request = self.factory.get(path=url)
        request.user = user
        response = forum_edit_view(request, forum.pk)
        self.assertEqual(response.status_code, 200)

    def test_forum_edit_comment_view(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=user.profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )
        comment = Comment.objects.create(
            forum=forum,
            comment_author=user.profile,
            comment_content='Good Post'
        )

        payload = {
            'comment_content': 'Sorry!'
        }
        url = reverse('forum:forum_comment_edit', args=[forum.pk, comment.pk])
        request = self.factory.post(path=url, data=payload)
        request.user = user
        response = forum_comment_edit_view(request, forum.pk, comment.pk)
        response.client = Client()
        self.assertRedirects(response, reverse('forum:forum_single', args=[forum.pk]))

    # def test_forum_edit_comment_view_with_different_comment_author(self):
    #     user = User.objects.create_user(
    #         username='john',
    #         email='john.doe@gmail.com',
    #         password='testing123',
    #     )
    #     another_user = User.objects.create_user(
    #         username='sissy',
    #         email='sissy@gmail.com',
    #         password='testing123',
    #     )
    #     category = Category.objects.create(category_title='Testing')
    #     forum = Forum.objects.create(
    #         forum_author=user.profile,
    #         forum_title='Test new thread.',
    #         forum_category=category,
    #         forum_content='Lorep insum dolor amet.',
    #     )
    #     comment = Comment.objects.create(
    #         forum=forum,
    #         comment_author=user.profile,
    #         comment_content='Good Post'
    #     )
    #
    #     with self.assertRaises(PermissionDenied):
    #         url = reverse('forum:forum_comment_edit', args=[forum.pk, comment.pk])
    #         request = self.factory.get(path=url)
    #         request.user = another_user
    #         forum_comment_edit_view(request, forum.pk, comment.pk)

    def test_retrieve_forum_edit_comment_form_view(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=user.profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )
        comment = Comment.objects.create(
            forum=forum,
            comment_author=user.profile,
            comment_content='Good Post'
        )
        url = reverse('forum:forum_comment_edit', args=[forum.pk, comment.pk])
        request = self.factory.get(path=url)
        request.user = user
        response = forum_comment_edit_view(request, forum.pk, comment.pk)
        self.assertEqual(response.status_code, 200)



