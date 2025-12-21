from django.db import models

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        unique_slugify(self, value=self.title)
        super().save()


class Link(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url
