from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from bestofblocket.core.views import (
    AdsDetailJsonView,
    AdSitemap,
    AdsListJsonView,
    AdView,
    HomePageView,
    RandomAdDetailJsonView,
    RandomAdView,
    RandomGen3AdView,
    TextTemplateView,
)

sitemaps = {
    "ads": AdSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="index"),
    path(
        "api/v1/ads/random/",
        RandomAdDetailJsonView.as_view(),
        name="ads-detail-random-json",
    ),
    path("api/v1/ads/<int:pk>/", AdsDetailJsonView.as_view(), name="ads-detail-json"),
    path(
        "api/v1/ads/<slug:slug>/",
        AdsDetailJsonView.as_view(),
        name="ads-lookup-by-slug-json",
    ),
    path("api/v1/ads/", AdsListJsonView.as_view(), name="ads-list-json"),
    path("slumpa/gen3/", RandomGen3AdView.as_view(), name="randomgen3"),
    path("slumpa/", RandomAdView.as_view(), name="random"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("robots.txt", TextTemplateView.as_view(template_name="robots.txt")),
    path("ads.txt", TextTemplateView.as_view(template_name="ads.txt")),
    path(
        "privacypolicy/",
        TemplateView.as_view(template_name="app_privacy_policy.html"),
    ),
    path("<slug:slug>/", AdView.as_view(), name="ad"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
