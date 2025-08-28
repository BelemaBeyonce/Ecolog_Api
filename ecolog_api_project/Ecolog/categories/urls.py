from django.urls import path
from .views import CategoryListView, CategoryTopicsView # Corrected from TopicListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'), #for listing categories and allowing users to search them.

    path('<int:pk>/topics/', CategoryTopicsView.as_view(), name='category-topics'),
    #for retrieving topics that belong to a specific category.
]