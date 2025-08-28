from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Topic, Favorite 
from .serializers import TopicSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicDetailView(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicRelatedTopicsView(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        topic_id = self.kwargs.get('pk')
        topic = get_object_or_404(Topic, id=topic_id)
        return Topic.objects.none()
    
class TopicFavoriteView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        topic = get_object_or_404(Topic, id=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, topic=topic)
        if not created:
            return Response({"detail": "Topic already in favorites."}, status=status.HTTP_409_CONFLICT)
        return Response({"detail": "Topic added to favorites."}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        topic = get_object_or_404(Topic, id=pk)
        try:
            favorite = Favorite.objects.get(user=request.user, topic=topic)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response({"detail": "Topic not in favorites."}, status=status.HTTP_404_NOT_FOUND)

class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)



# Create your views here.
