from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from jobs.models import *
# Create your views here.
def index(request):
    return render(request,'jobs/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,5)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'jobs/hydjobs.html',{'jobs_list':jobs_list})

def blorejobs1(request):
    jobs_list=blorejobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,5)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'jobs/blorejobs.html',{'jobs_list':jobs_list})


def punejobs1(request):
    jobs_list=punejobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,5)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'jobs/punejobs.html',{'jobs_list':jobs_list})




def chennaijobs1(request):
    jobs_list=chennaijobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,5)
    page_number=request.GET.get('page')
    try:
        jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list=paginator.page(1)
    except EmptyPage:
        jobs_list=paginator.page(paginator.num_pages)
    return render(request,'jobs/chennaijobs.html',{'jobs_list':jobs_list})
