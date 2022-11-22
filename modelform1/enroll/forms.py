from django import forms
from .models import Useradmin
class StudentRegister(forms.ModelForm):
    class Meta:
        model=Useradmin
        fields =['email','name','pas']
