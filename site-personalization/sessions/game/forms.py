from django import forms


class MyIntForm(forms.Form):
    mytext = forms.IntegerField(max_value=100, min_value=0, label='Попробуйте угадать число')

    def clean(self):
        return self.cleaned_data
