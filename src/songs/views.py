# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from .models import Song

def index(request):

    songs = Song.objects.order_by('title')

    paginator = Paginator(songs, 50)
    page = request.GET.get('page')
    paged_songs = paginator.get_page(page)

    context = {
        'songs': paged_songs
    }

    return render(request, 'songs/index.html', context)
