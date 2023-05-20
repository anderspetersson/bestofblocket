from django.http import JsonResponse
from django.views.generic import ListView, DetailView, RedirectView, CreateView, TemplateView
from django.contrib.sitemaps import Sitemap
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import linebreaksbr
from bestofblocket.core.models import Ad, Link
from bestofblocket.core.forms import SubmitLinkForm
from braces.views import JSONResponseMixin


class HomePageView(ListView):
    """
    Render index page.
    """
    template_name = 'mobile/index.html'
    paginate_by = 10
    queryset = Ad.objects.filter(is_approved=True)


class AdsListJsonView(JSONResponseMixin, ListView):
    paginate_by = 10
    model = Ad

    def get_queryset(self):
        return Ad.objects.filter(generation=3, is_approved=True)

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """

        data = []
        for o in self.get_queryset():
            if o.image:
                data.append({
                    'id': o.pk,
                    'title': o.title,
                    'imageUrl': o.image.url,
                    'text': o.text
                })

        response_kwargs.setdefault("safe", False)
        return JsonResponse(
            data,
            **response_kwargs,
        )


class AdsDetailJsonView(JSONResponseMixin, DetailView):
    model = Ad

    def render_to_response(self, context, **response_kwargs):
        ad = self.get_object()
        data = {
            'id': ad.pk,
            'title': ad.title,
            'imageUrl': ad.image,
            'text': ad.text
        }

        response_kwargs.setdefault("safe", False)
        return JsonResponse(
            data,
            **response_kwargs,
        )


class MobileWebsiteView(TemplateView):
    template_name = 'mobile/index.html'


class AdView(DetailView):
    """
    Shows one ad.
    """

    model = Ad

    def get_template_names(self):
        return 'mobile/ad.html'


class RandomAdView(RedirectView):
    """
    Redirects to a random ad.
    """

    permanent = False

    def get_redirect_url(self, **kwargs):
        ad = Ad.objects.filter(is_approved=True).order_by('?')[0]
        return reverse('ad', args=(ad.slug, ))


class RandomGen3AdView(RedirectView):
    """
    Redirect to a random ad of generation 3. (Mobile optimized)
    """

    permanent = False

    def get_redirect_url(self, **kwargs):
        ad = Ad.objects.filter(is_approved=True, generation=3).order_by('?')[0]
        return reverse('ad', args=(ad.slug, ))


class SubmitLinkView(CreateView):
    """
    Let users submit links to blocket-ads.
    """

    template_name = 'submit.html'
    form_class = SubmitLinkForm

    def get_success_url(self):
        url = self.object.url.split('?')[0]
        ad = Ad.objects.get(link=url)
        return reverse('ad', kwargs={'slug': ad.slug})


class ThankView(TemplateView):
    """
    Thanks the user when he/she submits a link.
    """

    template_name = 'thanks.html'


class TextTemplateView(TemplateView):
    """
    Returns text. Used in robots.txt.
    """

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'text/plain'
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