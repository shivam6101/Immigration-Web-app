from django import forms
from .models import blog
class students_details(forms.ModelForm):
    class Meta:
        model=blog
        fields=['name','age','country','qualification','country','phone_no']
        
                