from django import forms
from .models import *


class ironForm(forms.Form):
    formNumber = forms.CharField(max_length=30)
    ironName = forms.CharField(max_length=30)
    ironPrice = forms.CharField(max_length=30)
    ironProfit = forms.CharField(max_length=30)
    Quality = forms.CharField(max_length=30)
    paymentDate = forms.CharField(max_length=30)
    dealAmount = forms.CharField(max_length=20)
    pickupAmount = forms.CharField(max_length=20)
    pickupCompany = forms.CharField(max_length=30)

    class Meta:
        model = IronData


class ProjectForm(forms.Form):
    projectName = forms.CharField(max_length=20)
    formNumber = forms.CharField(max_length=20)

    class Meta:
        model = projectInfo


class ExcelForm(forms.Form):
    formNumber = forms.CharField(max_length=20)
    time = forms.CharField(max_length=30)
    destination = forms.CharField(max_length=30)
    notes = forms.CharField(max_length=50)
    deliveryAmount = forms.CharField(max_length=20)
    deliveryPlate = forms.CharField(max_length=20)
    deliveryPerson = forms.CharField(max_length=20)
    deliveryPickFee = forms.CharField(max_length=20)

    class Meta:
        model = formData
