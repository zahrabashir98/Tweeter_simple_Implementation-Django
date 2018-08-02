from django import forms

class TwittForm(forms.Form):
    textfield = forms.CharField(widget=forms.Textarea)
   
  

