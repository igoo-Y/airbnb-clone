from django import forms
from django.forms.models import ModelChoiceField
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = ModelChoiceField(
        empty_label="Any Kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
