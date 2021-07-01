from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Data
from .forms import FoodForm
from django.db.models import Q



def dataModel(request):
    data = Data.objects.all().order_by('term')
    context = {
    'data': data,
    }
    return render(request, 'storage/index.html',context)

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


def allData(request):
    data = Data.objects.all().order_by('term')
    context = {
    'data': data,
    }
    return render(request, 'storage/all.html',context)


# 新規登録フォームHTMLへ返す
def showCreateForm(request):
    #フォームを変数にセット
    form = FoodForm()
    context = {
    'foodForm':form,
    }
    #データを渡す
    return render(request, 'storage/create.html',context)

# フォームから受取ったデータをDBに登録する
def addFood(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
    #リクエストをもとにフォームをインスタンス化
        foodForm = FoodForm(request.POST)
    if foodForm.is_valid():
        foodForm.save()
    #登録後、全件データを抽出
    data = Data.objects.all()
    context = {
    'data': data,
    'foodFrom':foodForm,
    }
    #user.htmlへデータを渡す
    return render(request, 'storage/all.html',context)

def dataDel(request,data_id):
    data = get_object_or_404(Data, id=data_id)
    data.delete()
    return redirect('../../../storage/all/')

def dataEdit(request, data_id):
    data = get_object_or_404(Data, id=data_id)
    if request.method == 'POST':
        foodForm = FoodForm(request.POST, instance=data)
        if foodForm.is_valid():
            foodForm.save()
            return redirect('../../../storage/all/')
    else:
        foodForm = FoodForm(instance=data)
        
    context = {
    'data': data,
    'foodForm':foodForm,
    }

    return render(request, 'storage/edit.html',context)
    