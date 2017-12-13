from django.conf.urls import include, url
from bestofblocket.core.views import HomePageView, AdView, RandomAdView, \
 AdSitemap, SubmitLinkView, ThankView, TextTemplateView, JSONListView, MobileWebsiteView, \
 RandomGen3AdView
from django.contrib.sitemaps.views import sitemap

from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'ads': AdSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='index'),

    url(r'^api/$', JSONListView.as_view(), name='jsonindex'),
    url(r'^mobile/$', MobileWebsiteView.as_view(), name='mobile'),
    url(r'^slumpa/gen3/$', RandomGen3AdView.as_view(), name='randomgen3'),
    url(r'^slumpa/$', RandomAdView.as_view(), name='random'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^tipsa/', SubmitLinkView.as_view(), name='submit'),
    url(r'^tack/', ThankView.as_view(), name='thanks'),
    url(r'^robots\.txt$', TextTemplateView.as_view(template_name="robots.txt")),
    url(r'(?P<slug>[^/]+)/$', AdView.as_view(), name='ad'),
]
