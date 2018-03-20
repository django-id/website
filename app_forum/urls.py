from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_forum'
urlpatterns = [
    path('', views.forum_list_view, name='forum_list'),
    path('thread/new/', views.forum_new_view, name='forum_new'),
    path('thread/<int:pk>/', views.forum_single_view, name='forum_single'),
    path('thread/<int:pk>/edit/', views.forum_edit_view, name='forum_edit'),
    path(
        'thread/<int:pk>/comment/edit/<int:id>/',
        views.forum_comment_edit_view,
        name='forum_comment_edit',
    ),
]

admin.site.site_header = 'Django-ID Dashboard'
