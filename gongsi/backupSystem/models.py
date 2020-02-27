from django.db import models


class formData(models.Model):
    formNumber = models.IntegerField()
    time = models.CharField(max_length=30, blank=True)
    destination = models.CharField(max_length=50, blank=True)
    notes = models.CharField(max_length=50, blank=True)
    deliveryAmount = models.CharField(max_length=20)
    deliveryPlate = models.CharField(max_length=20)
    deliveryPerson = models.CharField(max_length=20)
    deliveryPickFee = models.CharField(max_length=20)


class IronData(models.Model):
    formNumber = models.ForeignKey(formData, on_delete=models.CASCADE)
    ironName = models.CharField(max_length=30)
    ironPrice = models.CharField(max_length=30)
    ironProfit = models.CharField(max_length=30)
    Quality = models.CharField(max_length=30)
    paymentData = models.TimeField()
    dealAmount = models.CharField(max_length=20)
    pickupAmount = models.CharField(max_length=20)
    pickupCompany = models.CharField(max_length=30)


class projectInfo(models.Model):
    projectName = models.CharField(max_length=20)
    form = models.ManyToManyField(formData)
