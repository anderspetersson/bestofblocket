from django.urls import include, path

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
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='index'),
    path('api/', JSONListView.as_view(), name='jsonindex'),
    path('mobile/', MobileWebsiteView.as_view(), name='mobile'),
    path('slumpa/gen3/', RandomGen3AdView.as_view(), name='randomgen3'),
    path('slumpa/', RandomAdView.as_view(), name='random'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('tipsa/', SubmitLinkView.as_view(), name='submit'),
    path('tack/', ThankView.as_view(), name='thanks'),
    path('robots.txt', TextTemplateView.as_view(template_name="robots.txt")),
    path('ads\.txt', TextTemplateView.as_view(template_name="ads.txt")),
    path('<slug:slug>/', AdView.as_view(), name='ad'),
]
