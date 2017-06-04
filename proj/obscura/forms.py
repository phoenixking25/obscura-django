from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 
from django import forms


class GetInfo(forms.Form):
	college = forms.CharField(help_text = "Enter your college/institution name.")
	location = forms.CharField(help_text = "Enter your location	.")
	phone = forms.CharField(help_text = "Enter your phone number.")


class GetAns(forms.Form):
    ans = forms.CharField(help_text="Enter your ans")
