from django import forms


class WikiCreate(forms.Form):
    name = forms.TimeField
    topic = forms.TimeField
