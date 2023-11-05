from django.shortcuts import render, redirect, get_object_or_404

# from database information saved, import all of Places that is there
from .models import Place

# Forms page
from .forms import NewPlaceForm


# This function will be called by django and give that function information what the  client requests it's making.
# Combine template and data here


def place_list(request):

    # Another way to handle POST requests, which makes a new place object form USING the existing  data requests, and then redirect users to the same page (Essentially reload ) and show the new place added

    if request.method == 'POST':
        # Make a new place form object from users request (A place to add which is a POST method, data from the page)
        form = NewPlaceForm(request.POST)

        # Create a model place object from the form's req. data
        place = form.save()

        # Validation - A method to check if the form is a good, then save the place and then "reload" the same page with the newly added place. This is against DB constraints
        if form.is_valid():
            place.save()  # Save place to DB

            # Reloading the place list (home page)
            return redirect('place_list')

    # Note: If the request is a "GET" method, then the top function is skipped and directly goes to this function belows
    # Places data from models
    # Django's ORM
    # We are using filter method and order_by method to filter only places that is not visited and sort them by name
    users_places = Place.objects.filter(visited=False).order_by('name')

    # Forms

    new_place_form = NewPlaceForm()  # To create HTML

    # Render that request information by  sending that information to templates - The page the client sees
    # Clients req is recognized From travel_wishlist urls path in the 'wishlist' dir routing to urls.py in travel_wishlist dir routes to views.py (here) and then routes AND render to templates wishlist.html
    return render(request, 'travel_wishlist/wishlist.html', {'users_places': users_places, 'new_place_form': new_place_form})


# Visited page
def places_visited(request):
    visited = Place.objects.filter(visited=True)

    return render(request, 'travel_wishlist/visited.html', {
        'visited_places': visited
    })


# User requests for About information and will be routed to about.html
def about(request):

    # Data to send to about page
    author = 'Jay'
    about = 'A website to create a list of places to visit'
    thankyouMessage = 'Thank you for using this web application!'

    return render(request, 'travel_wishlist/about.html', {
        'author': author, 'about': about,
        'thankyouMessage': thankyouMessage,
    })


# This place was visited function will need to know the users request AND the primary key of that request of visited place
def place_was_visited(request, place_primary_key):
    if request.method == 'POST':
        # Get that primary key from that object
        # place = Place.objects.get(pk=place_primary_key)

        # A combined method from Django where get the object and that specific key-value pair or give back a status code 400 if not found. This is so if that place with that primary key is not found, the app wouldn't crash. Instead, it would give a status code 400
        place = get_object_or_404(Place, pk=place_primary_key)

        place.visited = True

        place.save()  # Always need to save to db for any changes made

    # Redirect to place list when the save request is finished
    return redirect('place_list')
