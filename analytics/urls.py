from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^analytics/$', 'analytics.views.dashboard', name='dashboard'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^blog/(\d+)/$', 'blog.views.post', name='post'),
    url(r'^blog/(?P<tag_name>\w+)/$', 'blog.views.blog_tag', name='blog_tag'),
    url(r'^blog/(?P<author_pk>\d+)/$', 'blog.views.blog_author', name='blog_author'),
    url(r'^error/$', 'analytics.views.error', name='error')
)