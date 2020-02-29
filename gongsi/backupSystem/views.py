import xlwt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import urlquote
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
        allIronData[data['ironName']] = data

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
    return render(request, 'manage.html')


def sendDataBack(request):
    if request.POST.get('action') == 'POST':
        return JsonResponse(allIronData[str(request.POST.get('ironName'))])
    return "error"


def searchByForm(request):
    if request.POST.get('action') == 'POST':
        formId = request.POST.get('formId')
        filteredForm = list(formData.objects.filter(formNumber=str(formId)).values())
        filteredProject = list(projectInfo.objects.filter(formNumber=str(formId)).values())
        filteredIron = list(IronData.objects.filter(formNumber=str(formId)).values())
        response_data = {"project": filteredProject, "form": filteredForm, "iron": filteredIron}

        return JsonResponse(response_data, safe=False)


def modifyIronData(request):
    if request.POST.get('action') == 'POST':
        formNumber = request.POST.get('formNumber')
        ironName = request.POST.get('ironName')
        targetData = IronData.objects.get(formNumber=str(formNumber), ironName=str(ironName))
        targetData.ironName = request.POST.get('NewIronName')
        targetData.ironPrice = request.POST.get('ironPrice')
        targetData.Quality = request.POST.get('Quality')
        # form.totalPrice = request.POST.get('totalPrice') if not None else "Null"
        targetData.ironProfit = request.POST.get('ironProfit')
        targetData.paymentDate = request.POST.get('paymentDate')
        targetData.dealAmount = request.POST.get('dealAmount')
        targetData.pickupAmount = request.POST.get('pickupAmount')
        targetData.pickupCompany = request.POST.get('pickupCompany')
        targetData.save()

        return render(request, 'manage.html')
    return "failed"


def export_users_xls(request):
    filename = u"所以项目单数据"
    filename = urlquote(filename)
    wb = xlwt.Workbook(encoding='utf-8')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename + '.xls'
    ws = wb.add_sheet('所有项目单数据')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['项目名称', '送货单编号', '钢材规格',
               '送货时间', '目的地', '运费', '车号',
               '单价', '数量', '毛利润', '付款日期',
               '交货数量', '提货数量', '提货公司',
               '运输人', '吊装费', '备注']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    allIron = IronData.objects.all()
    writerData = []
    for data in allIron:
        formNumber = data.formNumber
        ironName = data.ironName
        ironPrice = data.ironPrice
        ironProfit = data.ironProfit
        Quality = data.Quality
        paymentDate = data.paymentDate
        dealAmount = data.dealAmount
        pickupAmount = data.pickupAmount
        pickupCompany = data.pickupCompany
        projectName = projectInfo.objects.get(formNumber=formNumber).projectName
        time = formData.objects.get(formNumber=formNumber).time
        destination = formData.objects.get(formNumber=formNumber).destination
        deliveryAmount = formData.objects.get(formNumber=formNumber).deliveryAmount
        deliveryPlate = formData.objects.get(formNumber=formNumber).deliveryPlate
        deliveryPerson = formData.objects.get(formNumber=formNumber).deliveryPerson
        deliveryPickFee = formData.objects.get(formNumber=formNumber).deliveryPickFee
        notes = formData.objects.get(formNumber=formNumber).notes
        writerData.append((projectName, formNumber, ironName, time, destination,
                           deliveryAmount, deliveryPlate, ironPrice, Quality,
                           ironProfit, paymentDate, dealAmount, pickupAmount,
                           pickupCompany, deliveryPerson, deliveryPickFee, notes
                           )
                          )

    for row in writerData:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
