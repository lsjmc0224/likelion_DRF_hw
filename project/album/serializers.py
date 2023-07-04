from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    tracks = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        tracks = instance.tracks.all()
        return [track.title for track in tracks]

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'description', 'year', 'tracks']

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField(read_only=True)

    def get_album(self, instance):
        return instance.album.title
    
    class Meta:
        model = Track
        exclude = ['id']
        read_only_fields = ['album']