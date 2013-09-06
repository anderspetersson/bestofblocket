from django.views.generic import ListView, DetailView, RedirectView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from bestofblocket.core.models import Ad


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