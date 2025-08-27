from rest_framework import serializers
from .models import Topic, Favorite
from categories.serializers import CategorySerializer
from users.serializers import UserSerializer

class TopicSerializer(serializers.ModelSerializer):
    # Nested serializer to show the full category object
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = '__all__'