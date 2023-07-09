from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    year = models.PositiveIntegerField()

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.CASCADE, related_name='tracks')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=50)