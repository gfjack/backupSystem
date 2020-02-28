from django.urls import path
from . import views

urlpatterns = [
    path('', views.addProject, name='add-project'),
    path('getData/', views.getData, name='getData'),
    path('getProjectData/', views.getProjectData, name='getProjectData'),
    path('delete/', views.deleteAllData, name='deleteAllData'),
    path('management/', views.renderManagement, name='manage'),
]
