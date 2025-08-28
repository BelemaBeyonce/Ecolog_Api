from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from topics.models import Topic
from topics.serializers import TopicSerializer
from django.shortcuts import get_object_or_404

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryTopicsView(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        category = get_object_or_404(Category, id=category_id)
        return Topic.objects.filter(category=category)
# Create your views here.
