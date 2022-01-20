from logging import PlaceHolder
from django import forms

from .models import Stock

class StockAddForm(forms.ModelForm):

    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"placeholder":"Enter company/stock name",
                                                                        "class":"form-control",
                                                                        "list":"datalistOptions",
                                                                        "id":"exampleDataList colFormLabel"
                                                                        }))

    quantity = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"ex: 12", "class":"form-control", "id":"colFormLabel"}))

    buy_price = forms.DecimalField(decimal_places=2, max_digits=10000, widget=forms.TextInput(attrs={"placeholder":"ex: 625.85", "class":"form-control", "id":"colFormLabel"}))

    buy_date = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y', attrs={"placeholder":"ex: 25-02-2018", "class":"form-control", "id":"colFormLabel"}),
                                                    input_formats=['%d-%m-%Y'])

    class Meta:
        model = Stock
        fields = [
            'name',
            'quantity',
            'buy_price',
            'buy_date',
        ]