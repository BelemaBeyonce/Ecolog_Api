from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Topic, Favorite
from .serializers import TopicSerializer, FavoriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsOwnerOrReadOnly

class TopicListView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'content']
    permission_classes = [IsAuthenticated] # Only authenticated users can create topics
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #adding permissions here to ensure only the owner can edit/delete
    

class TopicFavoriteView(generics.GenericAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, topic=topic)
        
        if not created:
            return Response({"detail": "Topic already in favorites."}, status=status.HTTP_409_CONFLICT)
        
        return Response({"detail": "Topic added to favorites."}, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        topic_id = self.kwargs.get('id')
        topic = get_object_or_404(Topic, id=topic_id)
        serializer.save(user=self.request.user, topic=topic)

    def delete(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
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