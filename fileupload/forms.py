from django import forms

class ProfileForm(forms.Form):
   passp = forms.CharField(max_length = 100)
   passpic = forms.ImageFields()
   licen = forms.CharField(max_length=100)
   licenpic = forms.ImageFields()
   aadha = forms.CharField(max_length=100)
   aadhapic = forms.ImageFields()