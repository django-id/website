from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^@(?P<slug>[-\w]+)/$', views.author_single_view, name='author_single'),
    url(r'^@(?P<slug>[-\w]+)/edit/$', views.author_edit_view, name='author_edit'),
]
