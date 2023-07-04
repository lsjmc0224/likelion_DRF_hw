from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    tracks = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        serializer = TrackSerializer(instance.tracks, many=True)
        return serializer.data

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'description', 'year', 'tracks']

class TrackSerializer(serializers.ModelSerializer):

    # album = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['album']