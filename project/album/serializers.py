from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    tracks = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        tracks = instance.tracks.all()
        return [track.title for track in tracks]
    
    tag = serializers.SerializerMethodField()
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Album
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField(read_only=True)

    def get_album(self, instance):
        return instance.album.title
    
    class Meta:
        model = Track
        exclude = ['id']
        read_only_fields = ['album']