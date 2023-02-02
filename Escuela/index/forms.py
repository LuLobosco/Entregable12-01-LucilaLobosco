from django import forms
from index.models import ImageIndex

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = ImageIndex
        fields = ['name','index_picture']