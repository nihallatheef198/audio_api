from rest_framework import serializers
from .models import song, podcast, audio_book

class song_serializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = '__all__'


class podcast_serializer(serializers.ModelSerializer):
    class Meta:
        model = podcast
        fields = '__all__'


class audio_book_serializer(serializers.ModelSerializer):
    class Meta:
        model = audio_book
        fields = '__all__'
