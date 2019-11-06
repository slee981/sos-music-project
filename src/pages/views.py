# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    form_register_class = UserCreationForm
    return render(request, 'pages/index.html', {'form_register': form_register_class})

def about(request):
    return render(request, 'pages/about.html')
