from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from ..core.api import api

from bestofblocket.core.views import (
    AdSitemap,
    AdView,
    HomePageView,
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
    path("slumpa/gen3/", RandomGen3AdView.as_view(), name="randomgen3"),
    path("slumpa/", RandomAdView.as_view(), name="random"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("robots.txt", TextTemplateView.as_view(template_name="robots.txt")),
    path("ads.txt", TextTemplateView.as_view(template_name="ads.txt")),
    path("<slug:slug>/", AdView.as_view(), name="ad"),
    path("api/", api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
