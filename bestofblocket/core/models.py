from django.db import models
from bestofblocket.core.utils import unique_slugify


class Ad(models.Model):
    filnamn = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    date = models.DateTimeField()
    tips_author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ads/')
    generation = models.SmallIntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['-pk']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def save(self, **kwargs):
        unique_slugify(self, value=self.title)
        super(Ad, self).save()


class Link(models.Model):
    url = models.URLField()

    def __unicode__(self):
        return url
