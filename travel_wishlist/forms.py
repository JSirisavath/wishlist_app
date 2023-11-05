from django import forms
from .models import Place


# Forms.ModelForm is a form for the webpage and related to the models
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')
