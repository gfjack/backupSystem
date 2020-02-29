from django.urls import path
from . import views

urlpatterns = [
    path('', views.addProject, name='add-project'),
    path('getData/', views.getData, name='getData'),
    path('getProjectData/', views.getProjectData, name='getProjectData'),
    path('delete/', views.deleteAllData, name='deleteAllData'),
    path('management/', views.renderManagement, name='manage'),
    path('searchByForm/', views.searchByForm, name='searchByForm'),
    path('sendDataBack/', views.sendDataBack, name='sendDataBack'),
    path('modifyData/', views.modifyIronData, name='modifyIronData'),
    path('export/', views.export_users_xls, name='export'),
]
