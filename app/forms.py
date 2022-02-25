from dataclasses import fields
from django import forms
from .models import lib,Book

class Userform(forms.ModelForm):
    
    class Meta:
        model = lib
        fields = ("__all__")

        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
class Bookform(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ("__all__")
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'})
        }
        
       
        
        