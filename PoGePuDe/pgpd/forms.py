'''
Created on Aug 3, 2018

@author: ALI
'''
from django import forms
from pgpd.models import Devices 
class DevicesForm(forms.ModelForm):
    class Meta:
        model = Devices
        #fields = "__all__"
        fields = ('devicename','devicemodel','devicedsc')