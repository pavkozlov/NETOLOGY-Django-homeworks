from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    def __init__(self, request, pk, *args, **kwargs):
        self.request = request
        self.pk = pk
        super(ReviewForm, self).__init__(*args, **kwargs)

    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    def clean(self):
        pk = self.pk
        reviewed_products = self.request.session['reviewed_products']
        if pk in reviewed_products:
            raise forms.ValidationError({'text': "Вы уже писали обзор на этот товар!"})
        return self.cleaned_data

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
