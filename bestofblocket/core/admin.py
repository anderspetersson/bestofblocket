from django.contrib import admin
from bestofblocket.core.models import Ad, Link

class AdAdmin(admin.ModelAdmin):
    search_fields = ['title', 'filnamn']

admin.site.register(Ad, AdAdmin)
admin.site.register(Link)