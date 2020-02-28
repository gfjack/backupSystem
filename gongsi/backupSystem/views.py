from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# 主页
def addProject(request):
    return render(request, 'index.html')


# 读取钢材信息表格数据
data = {}


# 收取钢材信息
def getData(request):
    response_data = {}
    if request.POST.get("action") == 'POST':
        data['ironName'] = request.POST.get('ironName')
        data['ironPrice'] = request.POST.get('ironPrice')
        data['Quality'] = request.POST.get('Quality')
        # form.totalPrice = request.POST.get('totalPrice') if not None else "Null"
        data['ironProfit'] = request.POST.get('ironProfit')
        data['paymentDate'] = request.POST.get('paymentDate')
        data['dealAmount'] = request.POST.get('dealAmount')
        data['pickupAmount'] = request.POST.get('pickupAmount')
        data['pickupCompany'] = request.POST.get('pickupCompany')
    response_data['ironName'] = request.POST.get('ironName')
    return JsonResponse(response_data)


# 收集项目和发货单信息
def getProjectData(request):
    if request.method == 'POST':
        form = IronData()
        form.formNumber = request.POST.get('formNumber')
        form.ironName = data['ironName']
        form.ironPrice = data['ironPrice']
        form.Quality = data['Quality']
        form.ironProfit = data['ironProfit']
        form.paymentDate = data['paymentDate']
        form.dealAmount = data['dealAmount']
        form.pickupAmount = data['pickupAmount']
        form.pickupCompany = data['pickupCompany']
        data.clear()
        projectForm = ProjectForm(request.POST)
        excelForm = ExcelForm(request.POST)

        # print(form.formNumber)
        # print(form.ironName)
        # print(form.ironPrice)
        # print(form.Quality)
        # print(form.ironProfit)
        # print(form.paymentDate)
        # print(form.dealAmount)
        # print(form.pickupAmount)
        # print(form.pickupCompany)
        # print(projectForm)

        # projectForm.projectName = request.POST.get('projectName')
        # projectForm.formNumber = request.POST.get('formNumber')
        # excelForm.formNumber = request.POST.get('formNumber')
        # excelForm.time = request.POST.get('time')
        # excelForm.destination = request.POST.get('destination')
        # excelForm.notes = request.POST.get("notes")
        # excelForm.deliveryAmount = request.POST.get('deliveryAmount')
        # excelForm.deliveryPlate = request.POST.get('deliveryPlate')
        # excelForm.deliveryPerson = request.POST.get('deliveryPerson')
        # excelForm.deliveryPickFee = request.POST.get('deliveryPickFee')

        # print(excelForm.formNumber)
        # print(excelForm.time)
        # print(excelForm.destination)
        # print(excelForm.notes)
        # print(excelForm.deliveryAmount)
        # print(excelForm.deliveryPlate)
        # print(excelForm.deliveryPerson)
        # print(excelForm.deliveryPickFee)

        # 存进数据库
        if excelForm.is_valid() and projectForm.is_valid():
            excelForm.save()
            projectForm.save()
            form.save()

            # print(form.formNumber)
            # print(projectForm.formNumber)
            # print(excelForm.formNumber)
            # form.save(commit=True)
            # projectForm.save(commit=True)
            # excelForm.save(commit=True)
    return redirect(addProject)


def deleteAllData(request):
    formData.objects.all().delete()

    return HttpResponse('deleted')


def renderManagement(request):
    return render(request, 'management.html')