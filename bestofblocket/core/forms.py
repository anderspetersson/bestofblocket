# -*- coding: utf-8 -*-
from django import forms
from bestofblocket.core.models import Link
class SubmitLinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['url']
        widgets = {
        'url': forms.TextInput(attrs={
            'placeholder': 'Fyll i din länk, t.ex. http://www.blocket.se/stockholm/haftig_grej_20111.htm?ca=11&w=1'
            })
        }