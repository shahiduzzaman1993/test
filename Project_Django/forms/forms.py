from django.db.models import fields
from forms.models import new_Forms
from django import forms

class new_Form(forms.ModelForm):
    class Meta:
        model = new_Forms
        fields = '__all__'
        