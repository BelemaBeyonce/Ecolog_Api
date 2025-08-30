from rest_framework import serializers
from .models import Topic, Favorite
from categories.serializers import CategorySerializer
from users.serializers import UserSerializer
import urllib.parse

class TopicSerializer(serializers.ModelSerializer):
    # Nested serializer to show the full category object
    category = CategorySerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    wikipedia_link = serializers.SerializerMethodField() #fielld for wikipedia link

    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'category', 'owner', 'created_at', 'wikipedia_link']

    def get_wikipedia_link(self, obj):
        encoded_title = urllib.parse.quote(obj.title.replace(' ', '_'))
        return f"https://en.wikipedia.org/wiki/{encoded_title}"
        #genertaing wikipedia link based on topic title, using the url to encode the title

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'topic']