from logging import PlaceHolder
from django import forms

from .models import Stock

class StockAddForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"placeholder":"Enter company/stock name"}))
    quantity = forms.IntegerField()
    buy_price = forms.DecimalField(decimal_places=2, max_digits=10000)
    a = forms.DateInput(format='%d-%m-%Y')
    # b = forms.TextInput(attrs={"placeholder":"date-month-year"})
    buy_date = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'), input_formats=['%d-%m-%Y'])

    class Meta:
        model = Stock
        fields = [
            'name',
            'quantity',
            'buy_price',
            'buy_date',
        ]