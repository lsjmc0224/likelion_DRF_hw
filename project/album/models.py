from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=200)

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.CASCADE, related_name='tracks')
    number = models.IntegerField()
    title = models.CharField(max_length=50)

