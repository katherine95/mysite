# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'resume/home.html')

def contact(request):
    return render(request, 'resume/contact.html', {'content':['If you would like to contact me,please email me', 'kathiekim95@gmail.com']})
