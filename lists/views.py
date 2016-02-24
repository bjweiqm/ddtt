#! /usr/bin/env python3
#encoding:utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#在这儿编写视图

def home_page(request):
    return render(request, 'home.html')
