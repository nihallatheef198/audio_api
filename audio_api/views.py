from django.http import HttpResponse
from . import models, serializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_data(request, type):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            if type == 'song':
                serializer_data = serializer.song_serializer(data=data)
                if serializer_data.is_valid():
                    serializer_data.save() 
            elif type == 'podcast':
                serializer_data = serializer.podcast_serializer(data=data)
                if serializer_data.is_valid():
                    serializer_data.save()
            elif type == 'audio_book':
                serializer_data = serializer.audio_book_serializer(data=data)
                if serializer_data.is_valid():
                    serializer_data.save()
            else:
                return HttpResponse(status=400)
            return HttpResponse(status=200)
        except Exception as e:
            # print(str(e))
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)



class view_update_delete_api(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        type = self.kwargs['type']
        if type == 'song':
            return models.song.objects.filter(pk=self.kwargs['pk'])
        elif type == 'podcast':
            return models.podcast.objects.filter(pk=self.kwargs['pk'])
        elif type == 'audio_book':
            return models.audio_book.objects.filter(pk=self.kwargs['pk'])

    def get_serializer(self, *args, **kwargs):
        type = self.kwargs['type']
        if type == 'song':
            serializer_class = serializer.song_serializer
            return serializer_class(*args, **kwargs)
        elif type == 'podcast':
            serializer_class = serializer.podcast_serializer
            return serializer_class(*args, **kwargs)
        elif type == 'audio_book':
            serializer_class = serializer.audio_book_serializer
            return serializer_class(*args, **kwargs)
