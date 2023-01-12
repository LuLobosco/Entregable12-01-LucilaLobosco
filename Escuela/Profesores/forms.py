from django import forms

class ProfesorForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    Materia = forms.CharField(max_length=100)
    activo = forms.BooleanField(required=False)