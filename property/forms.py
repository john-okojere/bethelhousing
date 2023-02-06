from django import forms
from .models import Uid, BasicInfo, DetailedInfo, ContactInfo, LocationInfo

class UidForm(forms.ModelForm):
    class Meta:
        model =Uid
        fields = ()
class BasicForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = ('title','status','type','price','area','bedroom','bathroom')

class LocationForm(forms.ModelForm):
    class Meta:
        model = LocationInfo
        fields  = ('address',)

class DetailedForm(forms.ModelForm):
    class Meta:
        model = DetailedInfo
        fields = ('description','age','garage','Room','airCondition','Bedding','Heating','Internet','Microwave','SmokingAllow','Terrace','Balcony','Icon','Wi_Fi','Beach','Parking')

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ('name', 'email','phone', 'gdpr')