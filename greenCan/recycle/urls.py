from django.urls import path

from . import views

app_name = 'recycle'

urlpatterns = [
    path('', views.index, name='index'),
    path('zipcode-search', views.search_locations_by_zipcode, name='search-location-zip'),
    path('currLoc-search', views.search_locations_by_current_location, name='search-location-currLoc'),
]