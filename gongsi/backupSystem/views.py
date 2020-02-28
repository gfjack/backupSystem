from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# 主页
def addProject(request):
    return render(request, 'index.html')


# 读取钢材信息表格数据
allIronData = {}


# 收取钢材信息
def getData(request):
    response_data = {'isExist': 0}
    data = {'flag': 0}
    if request.POST.get("action") == 'POST':

        if request.POST.get('ironName') in allIronData.keys():
            response_data['isExist'] = 1
        data['ironName'] = request.POST.get('ironName')
        data['ironPrice'] = request.POST.get('ironPrice')
        data['Quality'] = request.POST.get('Quality')
        # form.totalPrice = request.POST.get('totalPrice') if not None else "Null"
        data['ironProfit'] = request.POST.get('ironProfit')
        data['paymentDate'] = request.POST.get('paymentDate')
        data['dealAmount'] = request.POST.get('dealAmount')
        data['pickupAmount'] = request.POST.get('pickupAmount')
        data['pickupCompany'] = request.POST.get('pickupCompany')
        # print("存之前： ", allIronData)
        allIronData[data['ironName']] = data
        # print("存之后: ", allIronData)

    response_data['ironName'] = request.POST.get('ironName')
    return JsonResponse(response_data)


# 收集项目和发货单信息
def getProjectData(request):
    if request.method == 'POST':

        projectForm = ProjectForm(request.POST)
        excelForm = ExcelForm(request.POST)

        # 存进数据库
        if excelForm.is_valid() and projectForm.is_valid():
            excelForm.save()
            projectForm.save()
            tmpFormNumber = request.POST.get('formNumber')

            for data in allIronData:
                form = IronData()
                form.formNumber = tmpFormNumber
                form.ironName = allIronData[data]['ironName']
                form.ironPrice = allIronData[data]['ironPrice']
                form.Quality = allIronData[data]['Quality']
                form.ironProfit = allIronData[data]['ironProfit']
                form.paymentDate = allIronData[data]['paymentDate']
                form.dealAmount = allIronData[data]['dealAmount']
                form.pickupAmount = allIronData[data]['pickupAmount']
                form.pickupCompany = allIronData[data]['pickupCompany']
                form.save()
            allIronData.clear()

    return redirect(addProject)


def deleteAllData(request):
    formData.objects.all().delete()
    IronData.objects.all().delete()
    projectInfo.objects.all().delete()

    return redirect(addProject)


def renderManagement(request):
    return render(request, 'management.html')


def sendDataBack(request):
    # print(request.POST.get('ironName'))
    if request.POST.get('action') == 'POST':
        # print(allIronData[request.POST.get('ironName')])
        return JsonResponse(allIronData[str(request.POST.get('ironName'))])
    return "error"


def searchByForm(request):

    response = {'ok': "ok"}
    return JsonResponse(response)
