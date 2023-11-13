from django import forms
from .models import Place


# Forms.ModelForm is a form for the webpage and related to the models, which would then have access to the CRUD setup.
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')


# Using Django's built in date picker. Allows for more secure and easier date picker as well

class DateInput(forms.DateInput):
    input_type = 'date'


class TripReviewForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput()
        }
