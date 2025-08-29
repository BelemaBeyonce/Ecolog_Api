from django.urls import path
from .views import (
    TopicListView,
    TopicDetailView,
    TopicFavoriteView,
    FavoriteListView,
)

urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('<int:pk>/favorite/', TopicFavoriteView.as_view(), name='topic-favorite'),
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
]