from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser as User, Account


class SignUpForm(UserCreationForm):
    email =  forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'fullName', 'phone', 'email','accountType' , 'password1' , 'password2')

class EditprofileForm(forms.ModelForm):
    email =  forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'fullName', 'phone', 'email')


class AccountSignUpForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('yourTitle', 'address','city','state','zipcode','about','facebook','twitter','googlePlus','linkedIn')