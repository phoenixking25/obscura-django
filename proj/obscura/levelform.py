from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
from django import forms

class GetAns(forms.Form):
    ans = forms.CharField(help_text="Enter your ans")

    