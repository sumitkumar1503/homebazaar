from django import forms
from django.contrib.auth.models import User
from . import models

#for student related form
class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class CustomerExtraForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['mobile','address']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['englishname','hindiname','photo']


class ProductForm(forms.ModelForm):
    categoryid=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category", to_field_name="id")
    class Meta:
        model=models.Product
        fields=['englishname','hindiname','photo','price','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Order
        fields=['address','mobile']
        widgets = {
        'address':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

