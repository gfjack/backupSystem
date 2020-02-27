from django.http import JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *


# 主页
def addProject(request):
    return render(request, 'index.html')


# 收取钢材信息
def getData(request):
    response_data = {}
    if request.POST.get("action") == 'POST':
        form = ironForm(request.POST)

        # form.ironName = request.POST.get('ironName')
        # form.ironPrice = request.POST.get('ironPrice')
        # form.Quality = request.POST.get('Quality')
        # # form.totalPrice = request.POST.get('totalPrice')
        # form.ironProfit = request.POST.get('ironProfit')
        # form.paymentDate = request.POST.get('paymentDate')
        # form.dealAmount = request.POST.get('dealAmount')
        # form.pickupAmount = request.POST.get('pickupAmount')
        # form.pickupCompany = request.POST.get('pickupCompany')
        response_data['ironName'] = request.POST.get('ironName')
    return JsonResponse(response_data)


# 收集项目和发货单信息
def getProjectData(request):
    if request.method == 'POST':
        # form.formNumber = request.POST.get('formNumber')
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

        # if form.is_valid():
        #     print("1111111111111111111111111111111")

            # print(form.formNumber)
            # print(projectForm.formNumber)
            # print(excelForm.formNumber)
            # form.save(commit=True)
            # projectForm.save(commit=True)
            # excelForm.save(commit=True)
    return render(request, 'index.html')
