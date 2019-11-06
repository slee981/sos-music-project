# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from .models import Artist

def index(request):

    artists = Artist.objects.order_by('name')

    paginator = Paginator(artists, 50)
    page = request.GET.get('page')
    paged_artists = paginator.get_page(page)

    context = {
        'artists': paged_artists
    }

    return render(request, 'artists/index.html', context)
