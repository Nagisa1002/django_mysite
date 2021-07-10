from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import Data
from .forms import FoodForm
from .utils.paging import data_paging

def init_data():
    return Data.objects.all().order_by('term')

def all_data_view(request):
    context=data_paging(request,init_data())
    return render(request, 'storage/all.html', context)

def index_view(request):
    context=data_paging(request,init_data())
    return render(request, 'storage/index.html',context)

def match_data(request):
    data = init_data()
    word = request.GET.get('query')
    if word:
        data_list = data.filter(
                 Q(name=word)
               )
    context=data_paging(request,data_list)
    context['name']=word
    return render(request, 'storage/match.html',context)

# 新規登録フォームHTMLへ返す
def create_data(request):
    form = FoodForm()
    context = {
    'foodForm':form,
    }
    return render(request, 'storage/create.html',context)

# フォームから受取ったデータをDBに登録する
def add_data(request):
    if request.method == 'POST':
        foodForm = FoodForm(request.POST)
    if foodForm.is_valid():
        foodForm.save()
    return redirect('../../../storage/all/')


def del_data(request, data_id):
    data = get_object_or_404(Data, id=data_id)
    data.delete()
    return redirect('../../../storage/all/')

def edit_data(request, data_id):
    data = get_object_or_404(Data, id=data_id)
    if request.method == 'POST':
        foodForm = FoodForm(request.POST, instance=data)
        if foodForm.is_valid():
            foodForm.save()
            return redirect('../../../storage/all/')
    else:
        foodForm = FoodForm(instance=data)
        
    context = {
    'foodForm':foodForm,
    'data_id':data_id
    }
    return render(request,'storage/edit.html',context)

def detail_data(request, data_id):
    data = get_object_or_404(Data, id=data_id)
        
    context = {
    'data':data,
    'data_id':data_id
    }
    return render(request,'storage/detail.html',context)

