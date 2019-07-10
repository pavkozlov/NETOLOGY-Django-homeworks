from django import forms
from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_from = forms.CharField(label='Город:', widget=AjaxInputWidget(url='api/city_ajax'))
    city_to = forms.ChoiceField(choices=[(choice.pk, choice) for choice in City.objects.all()], label="Город прибытия")
    date = forms.DateField(widget=forms.SelectDateWidget, label='Дата')