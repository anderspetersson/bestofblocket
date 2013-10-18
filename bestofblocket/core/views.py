from django.views.generic import ListView, DetailView, RedirectView, CreateView, TemplateView
from django.shortcuts import redirect
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse, reverse_lazy
from bestofblocket.core.models import Ad, Link
from bestofblocket.core.forms import SubmitLinkForm

class HomePageView(ListView):
    """
    Render index page.
    """

    model = Ad
    template_name = 'index.html'
    paginate_by = 10


class AdView(DetailView):
    """
    Shows one ad.
    """

    model = Ad
    template_name = 'ad.html'


class RandomAdView(RedirectView):
    """
    Redirects to a random ad.
    """

    def get(self, request, *args, **kwargs):
        ad = Ad.objects.all().order_by('?')[0]
        slug = ad.slug
        print slug
        return redirect(reverse('ad', args=(ad.slug, )))


class SubmitLinkView(CreateView):
    """
    Let users submit links to blocket-ads.
    """

    model = Link
    template_name = 'submit.html'
    forms_class = SubmitLinkForm
    success_url = reverse_lazy('thanks')


class ThankView(TemplateView):
    template_name = 'thanks.html'


def setgenerationview(request, adid, gen):

    if request.user.is_superuser:

        ad = Ad.objects.get(id=adid)
        ad.generation = gen
        ad.save()

        return redirect('/slumpa/')


class TextTemplateView(TemplateView):
    """
    Returns text. Used in robots.txt.
    """

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'text/plain'
        return super(TemplateView, self).render_to_response(context, **response_kwargs)


class AdSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Ad.objects.all()

    def lastmod(self, obj):
        return obj.date