from django.db import models


class formData(models.Model):
    formNumber = models.CharField(max_length=20, null=True)
    time = models.CharField(max_length=30, default="待定")
    destination = models.CharField(max_length=50, default="待定")
    notes = models.CharField(max_length=50, null=True)
    deliveryAmount = models.CharField(max_length=20, null=True)
    deliveryPlate = models.CharField(max_length=20, null=True)
    deliveryPerson = models.CharField(max_length=20, null=True)
    deliveryPickFee = models.CharField(max_length=20, null=True)


class IronData(models.Model):
    formNumber = models.CharField(max_length=20)
    ironName = models.CharField(max_length=30, default="待定")
    ironPrice = models.CharField(max_length=30, null=True)
    ironProfit = models.CharField(max_length=30, null=True)
    Quality = models.CharField(max_length=30, null=True)
    paymentDate = models.CharField(max_length=20, null=True)
    dealAmount = models.CharField(max_length=20, null=True)
    pickupAmount = models.CharField(max_length=20, null=True)
    pickupCompany = models.CharField(max_length=30, null=True)


class projectInfo(models.Model):
    projectName = models.CharField(max_length=20, null=True)
    formNumber = models.CharField(max_length=20, null=True)
