from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^analytics/$', 'analytics.views.dashboard', name='dashboard'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
)