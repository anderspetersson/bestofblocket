from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, TemplateView

from bestofblocket.core.models import Ad


class HomePageView(ListView):
    """
    Render index page.
    """

    template_name = "index.html"
    paginate_by = 10
    queryset = Ad.objects.filter(is_approved=True)


class AdView(DetailView):
    """
    Shows one ad.
    """

    model = Ad

    def get_template_names(self):
        return "ad.html"


class RandomAdView(RedirectView):
    """
    Redirects to a random ad.
    """

    permanent = False

    def get_redirect_url(self, **kwargs):
        ad = Ad.objects.filter(is_approved=True).order_by("?")[0]
        return reverse("ad", args=(ad.slug,))


class SearchPageView(ListView):
    """
    Shows search results.
    """

    template_name = "search.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Ad.objects.filter(is_approved=True, title__icontains=query)
        return Ad.objects.filter(is_approved=True)


class RandomGen3AdView(RedirectView):
    """
    Redirect to a random generation 3 (mobile optimized) ad.
    """

    permanent = False

    def get_redirect_url(self, **kwargs):
        ad = Ad.objects.filter(is_approved=True, generation=3).order_by("?")[0]
        return reverse("ad", args=(ad.slug,))


class TextTemplateView(TemplateView):
    """
    Returns text. Used in robots.txt.
    """

    def render_to_response(self, context, **response_kwargs):
        response_kwargs["content_type"] = "text/plain"
        return super(TemplateView, self).render_to_response(context, **response_kwargs)


class AdSitemap(Sitemap):
    """
    Sitemap with all the Ads.
    """

    changefreq = "never"
    priority = 0.5

    def items(self):
        return Ad.objects.filter(is_approved=True)

    def lastmod(self, obj):
        return obj.date
