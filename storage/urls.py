from django.urls import path
from . import views

urlpatterns = [
path('', views.dataModel, name='dataModel'),
path('all/', views.allData, name='allData'),
path('create/', views.showCreateForm, name='showCreateForm'),
path('add/', views.addFood, name='addFood'),
path('del/<int:data_id>/', views.dataDel, name='dataDel'),
path('edit/<int:data_id>/',views.dataEdit, name='dataEdit'),
path('match/', views.dataMatch, name='dataMatch'),
]
