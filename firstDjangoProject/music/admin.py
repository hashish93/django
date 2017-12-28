from django.contrib import admin
from music.models import Album ,Song
# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_title', 'artist', 'genre']
    list_filter = ['album_title', 'artist', 'genre']



@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'album', 'file_type']
    list_filter = ['song_title', 'album', 'file_type']