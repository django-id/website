from django.urls import path

from . import views

app_name = 'app_author'
urlpatterns = [
    path('<slug:slug>/edit', views.author_edit_view, name='author_edit'),
    path('<slug:slug>', views.author_single_view, name='author_single'),
]
