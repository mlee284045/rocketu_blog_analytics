from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^blog/$', 'blog.views.error', name='blog'),
    url(r'^blog/(\d+)/$', 'blog.views.post', name='post'),
    url(r'^blog/(?P<tag_name>\w+)/$', 'blog.views.blog_tag', name='blog_tag'),
    url(r'^blog/(?P<author_pk>\d+)/$', 'blog.views.blog_author', name='blog_author'),
)
