from .models import Receipt
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#here are 3 forms i used 2 to create objects and one to update

class RegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class ReceiptForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields = ['store_name','date','item_list','total']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReceiptUpdateForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['store_name', 'date', 'item_list', 'total']
        