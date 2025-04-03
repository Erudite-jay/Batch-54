from django import forms
from . models import Contact

# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     message=forms.CharField(max_length=250)
#     file=forms.FileField()


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'