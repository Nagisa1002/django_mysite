from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import Data
from .forms import FoodForm
from .utils.paging import data_paging

def all_data_view(request):
    context=data_paging(request)
    return render(request, 'storage/all.html', context)

def index_view(request):
    context=data_paging(request)
    return render(request, 'storage/index.html',context)

def match_data(request):
    data_list = Data.objects.all().order_by('term')
    page_obj = paginate_queryset(request, data_list, 5)
    word = request.GET.get('query')
    if word:
        data = page_obj.object_list.filter(
                 Q(name=word)
               )

    context = {
        'data_list': data,
        'page_obj': page_obj,
    }
    return render(request, 'storage/match.html',context)

'''
def dataMatch(request):
    data = Data.objects.all()
    word = request.GET.get('query')
    if word:
        data = data.filter(
                 Q(name=word)
               )

    context = {
    'data': data,
    'word': word,
    }
    return render(request, 'storage/match.html',context)

'''

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


def del_data(request,data_id):
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
    }
    return render(request, 'storage/edit.html',context)
    