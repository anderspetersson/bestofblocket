# -*- coding: utf-8 -*-
from django import forms
from bestofblocket.core.models import Link


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
