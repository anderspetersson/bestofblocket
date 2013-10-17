from django.conf.urls import patterns, include, url
from bestofblocket.core.views import HomePageView, AdView, RandomAdView, setgenerationview, AdSitemap, SubmitLinkView, ThankView

from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'ads': AdSitemap,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bestofblocket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^slumpa/$', RandomAdView.as_view(), name='random'),
    url(r'^setgeneration/(?P<adid>[^/]+)/(?P<gen>[^/]+)/$', setgenerationview, name='setgeneration'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^tipsa/', SubmitLinkView.as_view(), name='submit'),
    url(r'^tack/', ThankView.as_view(), name='thanks'),
    url(r'(?P<slug>[^/]+)/$', AdView.as_view(), name='ad'),


)
