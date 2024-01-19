from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    artist_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.artist_name}"
    

class Album(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE , related_name='artists')
    title = models.CharField(max_length=128, unique=True)
    genre = models.TextField(blank=True, null=True)
    realised_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Music(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE , related_name='albums')
    music_name = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return self.music_name
    

class Music_detail(models.Model):
    music_id = models.OneToOneField(Music, on_delete=models.CASCADE)
    music_detail = models.TextField()
    
    def __str__(self):
        return self.music_name
