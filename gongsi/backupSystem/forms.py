from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    projectName = forms.CharField(max_length=20)
    formNumber = forms.CharField(max_length=20)

    class Meta:
        model = projectInfo
        fields = '__all__'


class ExcelForm(forms.ModelForm):
    formNumber = forms.CharField(max_length=20)
    time = forms.CharField(max_length=30)
    destination = forms.CharField(max_length=30)
    notes = forms.CharField(max_length=50, required=False)
    deliveryAmount = forms.CharField(max_length=20, required=False)
    deliveryPlate = forms.CharField(max_length=20, required=False)
    deliveryPerson = forms.CharField(max_length=20, required=False)
    deliveryPickFee = forms.CharField(max_length=20, required=False)

    class Meta:
        model = formData
        fields = '__all__'
