from django.shortcuts import render
from .forms import *
from django.forms import modelformset_factory
from .models import *


# 主页
def addProject(request):
    return render(request, 'index.html')


# 收取信息
def getData(request):
    pass

    # if request.method == 'POST':
    #     form = myForm(request.POST)
    #     if form.is_valid():
    #         pass
    #         # print(form.cleaned_data['projectName'])
    #         # print(form.cleaned_data['formNum'])
    #         # print(form.cleaned_data['time'])
    #         # print(form.cleaned_data['message'])
    # else:
    #     form = myForm()
    #
    # return render(request, 'index.html', {'form': form})


