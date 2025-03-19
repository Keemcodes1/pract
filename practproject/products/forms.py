from django import forms

class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField()
    image = forms.ImageField()
    quantity = forms.IntegerField()
   