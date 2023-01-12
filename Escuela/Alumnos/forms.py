from django import forms

class AlumnosForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    activo = forms.BooleanField(required=False)