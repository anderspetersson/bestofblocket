from django.contrib import admin
from bestofblocket.core.models import Ad, Link

class AdAdmin(admin.ModelAdmin):
    search_fields = ['title', 'filnamn']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Ad, AdAdmin)
admin.site.register(Link)