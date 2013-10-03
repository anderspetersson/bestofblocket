from django.contrib import admin
from bestofblocket.core.models import Ad

class AdAdmin(admin.ModelAdmin):
    search_fields = ['title', 'filnamn']

admin.site.register(Ad, AdAdmin)