import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class WikipediaSummaryView(APIView):
    """
    View to fetch summary of a topic from Wikipedia API.
    """
    def get(self, request, *args, **kwargs):
        query= request.query_params.get('q', None)
        if not query:
            return Response({'error': 'Query parameter "q" is required.'}, status=status.HTTP_400_BAD_REQUEST)
                    
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"

        headers = {
            'User-Agent': 'EcologApp/1.0 (belemaadim@gmail.com)'
        }
        

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status() # Raise an HTTP error for bad responses
            data = response.json()

            summary = {
                "title": data.get('title'),
                "extract": data.get('extract'),
                "source": "Wikipedia"
            }
            return Response(summary, status=status.HTTP_200_OK)
        
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class USGS_EarthquakeView(APIView):
    def get(self, request, *args, **kwargs):
        timeframe = request.query_params.get('timeframe', 'hour')
        
        # This will be the base URL
        url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{timeframe}.geojson"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # We can filter and return only the most relevant data
            features = data.get('features', [])
            earthquakes = []

            for feature in features:
                properties = feature.get('properties', {})
                earthquake = {
                    "magnitude": properties.get('mag'),
                    "place": properties.get('place'),
                    "time": properties.get('time'),
                    "url": properties.get('url'),
                    "source": "USGS"
                }
                earthquakes.append(earthquake)
            
            return Response(earthquakes, status=status.HTTP_200_OK)
        
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    