from django import forms
from .models import Product, Order



class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control border-2',})
        self.fields['contact'].widget.attrs.update({'class': 'form-control border-2'})
        self.fields['count'].widget.attrs.update({'class': 'form-control border-2'})
        self.fields['address'].widget.attrs.update({'class': 'form-control border-2',})
    class Meta:
        model = Order
        fields = ['count', 'name','contact','address', ]

