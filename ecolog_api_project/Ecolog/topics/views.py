from rest_framework import generics
from .models import Topic
from .serializers import TopicSerializer

class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

# Create your views here.
