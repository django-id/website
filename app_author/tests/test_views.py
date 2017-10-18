from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from app_author.views import author_single_view, author_edit_view


class AuthorViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_retrieve_author_single_view(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )

        url = reverse('author:author_single', args=[user.profile.slug])
        request = self.factory.get(path=url)
        response = author_single_view(request, user.profile.slug)
        self.assertEqual(response.status_code, 200)

    def test_author_edit_view(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        url = reverse('author:author_edit', args=[user.profile.slug])
        payload = {
            'profile_picture': None,
            'profile_name': 'Adit',
            'profile_email': 'adiyatmubarak@gmail.com',
            'profile_location': None,
            'profile_github': 'https://github.com/keda87',
        }

        request = self.factory.post(path=url, data=payload)
        request.user = user
        response = author_edit_view(request, user.profile.slug)
        response.client = Client()
        self.assertRedirects(
            response, reverse('author:author_single', args=[user.profile.slug])
        )

    def test_author_edit_view_form_with_another_user(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )
        another_user = User.objects.create_user(
            username='stranger',
            email='stranger@gmail.com',
            password='testing123',
        )

        url = reverse('author:author_edit', args=[user.profile.slug])
        request = self.factory.get(path=url)
        request.user = another_user
        response = author_edit_view(request, user.profile.slug)
        response.client = Client()
        self.assertRedirects(response, reverse('forum:forum_list'))

    def test_author_edit_view_form(self):
        user = User.objects.create_user(
            username='john',
            email='john.doe@gmail.com',
            password='testing123',
        )

        url = reverse('author:author_edit', args=[user.profile.slug])
        request = self.factory.get(path=url)
        request.user = user
        response = author_edit_view(request, user.profile.slug)
        response.client = Client()
        self.assertEqual(response.status_code, 200)

