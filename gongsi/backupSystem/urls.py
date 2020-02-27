from django.urls import path
from . import views

urlpatterns = [
    path('', views.addProject, name='add-project'),
    path('getData/', views.getData, name='getData'),
]
