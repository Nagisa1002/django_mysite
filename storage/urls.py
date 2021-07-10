from django.urls import path
from . import views

urlpatterns = [
path('', views.index_view, name='index_view'),
path('all/', views.all_data_view, name='all_data_view'),
path('create/', views.create_data, name='create_data'),
path('add/', views.add_data, name='add_data'),
path('del/<int:data_id>/', views.del_data, name='del_data'),
path('edit/<int:data_id>/',views.edit_data, name='edit_data'),
path('match/', views.match_data, name='match_data'),
path('detail/<int:data_id>/',views.detail_data, name='detail_data'),
]
