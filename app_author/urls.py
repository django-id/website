from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^@(?P<slug>[-\w]+)/$', views.author_single_view, name='author_single'),
    url(r'^@(?P<slug>[-\w]+)/edit/$', views.author_edit_view, name='author_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
