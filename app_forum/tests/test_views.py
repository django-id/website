from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from app_author.models import Profile
from app_forum.models import Category, Forum
from app_forum.views import forum_list_view, forum_new_view, forum_single_view


class ForumViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_retrieve_forum_list_view(self):
        url = reverse('forum_list')
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
        url = reverse('forum_new')
        payload = {
            'forum_title': 'Test new thread',
            'forum_category': category.pk,
            'forum_content': 'Lorep insum dolor amet.',
        }

        request = self.factory.post(path=url, data=payload)
        request.user = user
        response = forum_new_view(request)
        response.client = Client()
        self.assertRedirects(response, reverse('forum_list'))

    def test_retrieve_new_thread_form_view(self):
        user = User.objects.create_user(
            username='tester',
            email='tester@gmail.com',
            password='testing123',
        )
        url = reverse('forum_new')

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
        profile = Profile.objects.get(user=user)
        category = Category.objects.create(category_title='Testing')
        forum = Forum.objects.create(
            forum_author=profile,
            forum_title='Test new thread.',
            forum_category=category,
            forum_content='Lorep insum dolor amet.',
        )
        url = reverse('forum_single', args=[forum.pk])
        request = self.factory.get(path=url)
        response = forum_single_view(request, forum.pk)
        self.assertEqual(response.status_code, 200)

