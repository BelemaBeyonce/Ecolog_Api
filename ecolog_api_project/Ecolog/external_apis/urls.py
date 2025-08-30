from django.urls import path
from .views import WikipediaSummaryView, USGS_EarthquakeView

urlpatterns = [
    path('wikipedia-summary/', WikipediaSummaryView.as_view(), name='wikipedia-summary'),
    path('usgs-earthquakes/', USGS_EarthquakeView.as_view(), name='usgs'),
]