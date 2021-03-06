from django import forms
from currency.models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ('name', 'url', 'founded', 'address', 'contacts')
