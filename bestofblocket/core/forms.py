# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from bestofblocket.core.models import Link, Ad


class SubmitLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']

    def clean_url(self):
        """
        Check if the URL is from blocket.se
        """

        url = self.cleaned_data.get('url')
        if not 'blocket.se' in url:
            raise forms.ValidationError('Länken måste vara från blocket.se')
        return url

    def save(self, commit=True):
        """
        Make sure the same ad isnt submitted before.
        """

        link = self.cleaned_data.get('url')
        ad = Ad.objects.filter(link=link).first()
        if ad:
            return super(SubmitLinkForm, self).save(commit=False)
        else:
            return super(SubmitLinkForm, self).save(commit=True)
