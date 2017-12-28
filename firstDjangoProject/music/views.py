from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return HttpResponse(render(request,'music/index.html',context))

def detail(request, album_id):
    selected_album = get_object_or_404(Album, id=album_id)
    context = {'album': selected_album}
    return HttpResponse(render(request,'music/details.html',context))