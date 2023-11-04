# Path describes what an URL looks like
from django.urls import path

from . import views

# List of URL's that our app will know
urlpatterns = [
    # Any requests to the "home page" should be handled by the function called 'place_list' inside the views module
    # Note: The path the URL recognizes in this, is an empty url path string, so just local host/home page: http://127.0.0.1:8000/
    # The request from client being made is NOT admin page(url.py module from 'wishlist' dir) so it is this home page.
    path('', views.place_list, name='place_list'),

    path('visited', views.places_visited, name="places_visited"),

    # Make and Send the primary key of the place users visited to was visited
    # users Req to "place/<int:place_pk>/was_visited" to add that place to visited - This is for the home page if users have visited that place  from the wishlist
    path('place/<int:place_primary_key>/was_visited',
         views.place_was_visited, name='place_was_visited'),


    # About path
    path('about', views.about, name='about')
]
