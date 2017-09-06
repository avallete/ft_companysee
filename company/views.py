# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Company


def index(request):
    companies = Company.objects.all().order_by('name')
    paginator = Paginator(companies, 10)
    if request.method == 'POST' and request.POST.get('search'):
        companies = companies.filter(name__icontains=request.POST.get('search'))
        return render(request, 'index.html', {'data': companies})
    else:
        page = request.GET.get('page')
        try:
            companies = paginator.page(page)
        except PageNotAnInteger:
            companies = paginator.page(1)
        except EmptyPage:
            companies = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {'data': companies})
