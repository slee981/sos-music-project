# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from songs.models import SongComment, Song
from topics.models import SongTopic, Topic

# Create your views here.

from .models import Song

def songs_create_comment(request):
    comment = request.POST.get('comment', False)
    song_id = request.POST.get('song_id', False)
    user_id = request.user.id

    SongComment.objects.create(comment=comment, song_id=song_id, user_id=user_id)
    comments = SongComment.objects.filter(song_id = song_id)
    song = Song.objects.get(id = song_id)
    user_topics = SongTopic.objects.filter(user_id = user_id, song_id = song_id)

    user_topics_dict = []
    for user_topic in user_topics:
        user_topics_dict.append({'value': user_topic.topic.id, 'display': user_topic.topic.description})

    context = {
        'song': song,
        'comments': comments,
        'user_topics': user_topics_dict
    }

    return redirect('song', id=song_id)

def index(request):

    songs = Song.objects.order_by('title')

    paginator = Paginator(songs, 50)
    page = request.GET.get('page')
    paged_songs = paginator.get_page(page)

    context = {
        'songs': paged_songs
    }
    

    return render(request, 'songs/index.html', context)

def songs_search(request):
    q_objects = Q()
    
    # loop trough the list and create an OR condition for each item
    print(request.GET)
    text = request.GET.get('search_text', False)
    for field, value in request.GET:
        if (field == 'search_text'):
            q_objects.add(Q(title__icontains = value), Q.OR)
        # for our list_with_strings we can do the following
        # q_objects.add(Q(**{item: 1}), Q.OR)

    songs = Song.objects.filter(q_objects)
    context = {
        'songs': songs
    }

    return render(request, 'songs/index.html', context)


def song(request, id):

    song = Song.objects.get(id = id)
    user_id = request.user.id

    comments = SongComment.objects.filter(song_id = id).order_by('-created')
    user_topics = SongTopic.objects.filter(user_id = user_id, song_id = id)
    user_topics_dict = []
    for user_topic in user_topics:
        user_topics_dict.append({'value': user_topic.topic.id, 'display': user_topic.topic.description})

    context = {
        'song': song,
        'comments': comments,
        'user_topics': user_topics_dict
    }

    return render(request, 'songs/song.html', context)

def get_topics(request):
    topics = Topic.objects.order_by('description')
    topics_dic = []
    for topic in topics:
        topics_dic.append({'value': topic.id, 'display': topic.description})
    return JsonResponse(topics_dic, safe=False)

def save_song_topics(request):
    topics_post = request.POST.get('user_topics_form', False)
    song_id = request.POST.get('song_id', False)
    user_id = request.user.id
    topics = topics_post.split(',')

    for topic in topics:
        topic = Topic.objects.get(id = topic)
        SongTopic.objects.create(topic_id=topic.id, song_id=song_id, user_id=user_id)
    
    comments = SongComment.objects.filter(song_id = song_id)
    song = Song.objects.get(id = song_id)
    user_topics = SongTopic.objects.filter(user_id = user_id, song_id = song_id)
    
    user_topics_dict = []
    for user_topic in user_topics:
        user_topics_dict.append({'value': user_topic.topic.id, 'display': user_topic.topic.description})
    context = {
        'song': song,
        'comments': comments,
        'user_topics': user_topics_dict
    }

    #return render(request, 'songs/song.html', context)

    return redirect('song', id=song_id)
    