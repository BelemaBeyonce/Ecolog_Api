from django.urls import path
from .views import ( 
    TopicListView,
    TopicDetailView,
    TopicRelatedTopicsView,
    TopicFavoriteView,
    FavoriteListView,
)
                    

urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list'), #for listing topics and allowing users tosearch them.
    path('<int:pk>/related/', TopicRelatedTopicsView.as_view(), name='topic-related'), #for retrieving topics that are related to a specific topic.
    path('<int:pk>/favorite/', TopicFavoriteView.as_view(), name='topic-favorite'), #for adding a favorite topic or removing the topic from favorites.
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'), #listing all the users favorite topiscs
    


]