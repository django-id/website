from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.forum_list_view, name='forum_list'),
    url(r'^thread/new/$', views.forum_new_view, name='forum_new'),
    url(r'^thread/(?P<pk>[-\w]+)/$', views.forum_single_view, name='forum_single'),
    url(r'^thread/(?P<pk>[-\w]+)/edit/$', views.forum_edit_view, name='forum_edit'),
    url(r'^thread/(?P<pk>[-\w]+)/comment/edit/(?P<id>[-\w]+)/$', views.forum_comment_edit_view,
        name='forum_comment_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Django-ID Dashboard'
