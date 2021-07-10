from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Data


def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def data_paging(request,data_list):
    page_obj = paginate_queryset(request, data_list, 5)
    context = {
        'data_list': page_obj.object_list,
        'page_obj': page_obj,
    }
    return context
