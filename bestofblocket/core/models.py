from django.db import models
from django.core.mail import mail_admins
from bestofblocket.core.utils import unique_slugify


class Ad(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blocketimages/", blank=True, null=True)
    generation = models.SmallIntegerField(default=0, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    text = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-pk"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def save(self, **kwargs):
        unique_slugify(self, value=self.title)
        super(Ad, self).save()


class Link(models.Model):
    url = models.URLField()

    def __unicode__(self):
        return self.url

    def save(self, **kwargs):
        from bestofblocket.core.tasks import set_blocket_info

        ad = set_blocket_info(self.url)
        mail_admins(
            "Ny blocketannons",
            "En ny blocketannons har blivit tipsad: http://www.bestofblocket.se/admin/core/ad/%s/"
            % str(ad.id),
        )
        super(Link, self).save()
