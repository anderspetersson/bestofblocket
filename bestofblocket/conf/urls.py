from django.urls import path

from bestofblocket.core.views import HomePageView, AdView, RandomAdView, \
 AdSitemap, SubmitLinkView, ThankView, TextTemplateView, AdsListJsonView, \
 RandomGen3AdView, AdsDetailJsonView
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

sitemaps = {
    'ads': AdSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='index'),
    path('api/v1/ads/', AdsListJsonView.as_view(), name='ads-list-json'),
    path('api/v1/ads/<int:pk>/', AdsDetailJsonView.as_view(), name='ads-detail-json'),
    path('slumpa/gen3/', RandomGen3AdView.as_view(), name='randomgen3'),
    path('slumpa/', RandomAdView.as_view(), name='random'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('tipsa/', SubmitLinkView.as_view(), name='submit'),
    path('tack/', ThankView.as_view(), name='thanks'),
    path('robots.txt', TextTemplateView.as_view(template_name="robots.txt")),
    path('ads.txt', TextTemplateView.as_view(template_name="ads.txt")),
    path('<slug:slug>/', AdView.as_view(), name='ad'),
]

urlpatterns += staticfiles_urlpatterns()
