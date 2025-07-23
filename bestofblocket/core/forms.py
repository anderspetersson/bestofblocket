# -*- coding: utf-8 -*-
from django import forms
from bestofblocket.core.models import Link, Ad


class SubmitLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["url"]

    def clean_url(self):
        """
        Check if the URL is from blocket.se
        """

        url = self.cleaned_data.get("url")
        if "blocket.se" not in url:
            raise forms.ValidationError("Länken måste vara från blocket.se")
        return url

    def save(self, commit=True):
        """
        Make sure the same ad isnt submitted before.
        """

        link = self.cleaned_data.get("url")
        link = link.split("?")[0]
        ad = Ad.objects.filter(link=link).first()
        if ad:
            return super(SubmitLinkForm, self).save(commit=False)
        else:
            return super(SubmitLinkForm, self).save(commit=True)
