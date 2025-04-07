from django import forms
from .models import Products

# class ProductForm(forms.Form):
#     title = forms.CharField()
#     price = forms.DecimalField()
#     description = forms.CharField()
#     image = forms.ImageField()
#     quantity = forms.IntegerField()
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title','price','description','image','media','quantity']

        def clean_title(self):
            data = self.cleaned_data.get('title')
            if (len(data)) > 4:
                raise forms.ValidationError("Title must be more than 4 characters long.wutang")
            return data