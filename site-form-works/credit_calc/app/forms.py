from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара", min_value=1, required=True)
    rate = forms.IntegerField(label="Процентная ставка", min_value=1, required=True, max_value=100)
    months_count = forms.IntegerField(label="Срок кредита в месяцах", min_value=1, required=True)

    def clean(self):
        fields = [self.cleaned_data['initial_fee'], self.cleaned_data['rate'], self.cleaned_data['months_count']]
        for field in fields:
            if not field or field < 0:
                raise forms.ValidationError('Значение не  может быть пустым или нулевым')

        if self.cleaned_data['months_count'] >= self.cleaned_data['initial_fee']:
            raise forms.ValidationError({'months_count': 'Срок не может больше или равен меньше цены'})

        return self.cleaned_data
