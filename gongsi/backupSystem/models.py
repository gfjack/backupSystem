from django.db import models


class formData(models.Model):
    formNumber = models.CharField(max_length=20)
    time = models.CharField(max_length=30)
    destination = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    deliveryAmount = models.CharField(max_length=20)
    deliveryPlate = models.CharField(max_length=20)
    deliveryPerson = models.CharField(max_length=20)
    deliveryPickFee = models.CharField(max_length=20)


class IronData(models.Model):
    formNumber = models.CharField(max_length=30)
    ironName = models.CharField(max_length=30)
    ironPrice = models.CharField(max_length=30)
    ironProfit = models.CharField(max_length=30)
    Quality = models.CharField(max_length=30)
    paymentDate = models.CharField(max_length=20)
    dealAmount = models.CharField(max_length=20)
    pickupAmount = models.CharField(max_length=20)
    pickupCompany = models.CharField(max_length=30)


class projectInfo(models.Model):
    projectName = models.CharField(max_length=20)
    formNumber = models.CharField(max_length=20)
