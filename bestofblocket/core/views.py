from django.http import JsonResponse
from django.views.generic import ListView, DetailView, RedirectView, CreateView, TemplateView
from django.contrib.sitemaps import Sitemap
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import linebreaksbr
from django.core.paginator import Paginator
from django.shortcuts import render
from bestofblocket.core.models import Ad, Link
from bestofblocket.core.forms import SubmitLinkForm
from braces.views import JSONResponseMixin


class HomePageView(ListView):
    """
    Render index page.
    """
    template_name = 'index.html'
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
        paginator = Paginator(self.get_queryset(), 10)  # Show 25 contacts per page.
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        article_list = []
        for o in page_obj:
            if o.image:
                article_list.append({
                    'id': o.pk,
                    'slug': o.slug,
                    'title': o.title,
                    'image_url': o.image.url,
                    'text': o.text
                })
        data = {}
        data['articles'] = article_list
        if page_obj.has_next():
            data['next_page'] = page_obj.next_page_number()
        else:
            data['next_page'] = 1

        response_kwargs.setdefault("safe", False)
        return JsonResponse(
            data,
            **response_kwargs,
        )


class AdsDetailJsonView(JSONResponseMixin, DetailView):
    model = Ad
    query_pk_and_slug = True

    def render_to_response(self, context, **response_kwargs):
        ad = self.object
        next_random_article = Ad.objects.filter(generation=3, is_approved=True).exclude(image=None).order_by('?').first()
        data = {
            'id': ad.pk,
            'slug': ad.slug,
            'title': ad.title,
            'image_url': ad.image.url,
            'text': ad.text,
            'next_random_article_slug': next_random_article.slug
        }

        response_kwargs.setdefault("safe", False)
        return JsonResponse(
            data,
            **response_kwargs,
        )


class RandomAdDetailJsonView(AdsDetailJsonView):
    def get_object(self, queryset=None):
        return Ad.objects.filter(generation=3, is_approved=True).exclude(image=None).order_by('?').first()


class AdView(DetailView):
    """
    Shows one ad.
    """

    model = Ad

    def get_template_names(self):
        return 'ad.html'


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
    Redirect to a random generation 3 (mobile optimized) ad.
    """

    permanent = False

    def get_redirect_url(self, **kwargs):
        ad = Ad.objects.filter(is_approved=True, generation=3).order_by('?')[0]
        return reverse('ad', args=(ad.slug, ))


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
