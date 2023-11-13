from django.shortcuts import render, redirect, get_object_or_404

# from database information saved, import all of Places that is there
from .models import Place

# Forms page
from .forms import NewPlaceForm, TripReviewForm

# Django's built-in Authorization log-in method
from django.contrib.auth.decorators import login_required

# Can't have users request anything they are not suppose to make
from django.http import HttpResponseForbidden

from django.contrib import messages

# This function will be called by django and give that function information what the  client requests it's making.
# Combine template and data here
# Before any redirection to the html page for users, we want to make sure the decorator 'login-required' is required to all view functions before


@login_required
def place_list(request):

    # Another way to handle POST requests, which makes a new place object form USING the existing  data requests, and then redirect users to the same page (Essentially reload ) and show the new place added

    if request.method == 'POST':
        # Make a new place form object from users request (A place to add which is a POST method, data from the page)
        form = NewPlaceForm(request.POST)

        # Create a model place object from the form's req. data
        # Get that data, but don't save/commit it yet
        place = form.save(commit=False)

        # Users request to be that user that is signed in
        place.user = request.user

        # Validation - A method to check if the form is a good, then save the place and then "reload" the same page with the newly added place. This is against DB constraints
        if form.is_valid():
            place.save()  # Save place to DB

            # Reloading the place list (home page)
            return redirect('place_list')

    # Note: If the request is a "GET" method, then the top function is skipped and directly goes to this function belows
    # Places data from models
    # Django's ORM
    # We are using filter method and order_by method to filter only places that is not visited and sort them by name
    users_places = Place.objects.filter(
        user=request.user).filter(visited=False).order_by('name')

    # Forms

    new_place_form = NewPlaceForm()  # To create HTML

    # Render that request information by  sending that information to templates - The page the client sees
    # Clients req is recognized From travel_wishlist urls path in the 'wishlist' dir routing to urls.py in travel_wishlist dir routes to views.py (here) and then routes AND render to templates wishlist.html
    return render(request, 'travel_wishlist/wishlist.html', {'users_places': users_places, 'new_place_form': new_place_form})


# Visited page
@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)

    return render(request, 'travel_wishlist/visited.html', {
        'visited_places': visited
    })


# User requests for About information and will be routed to about.html
@login_required
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
@login_required
def place_was_visited(request, place_primary_key):
    if request.method == 'POST':
        # Get that primary key from that object
        # place = Place.objects.get(pk=place_primary_key)

        # A combined method from Django where get the object and that specific key-value pair or give back a status code 400 if not found. This is so if that place with that primary key is not found, the app wouldn't crash. Instead, it would give a status code 400
        place = get_object_or_404(Place, pk=place_primary_key)
        # We want to check if the user is the same as the user who is making requests - For security check
        if place.user == request.user:
            place.visited = True
            place.save()  # Always need to save to db for any changes made

        else:

            # If the requester is not the same as the "place_user"
            return HttpResponseForbidden()

    # Redirect to place list when the save request is finished
    return redirect('place_list')


# Place details for place detail page by getting that place primary id key
@login_required
def place_details(request, place_primary_key):
    place = get_object_or_404(Place, pk=place_primary_key)

    # Does this place belong to the current user?

    if place.user != request.user:
        return HttpResponseForbidden()

    # Is this a GET req? Or a POST req (update place)? or Both?

    # If POST req, validate form data and update.

    if request.method == 'POST':
        # Make a new form object with users data. So, when users are essentially in the page for the place details, and if users sends in a POST request, we want to create a new form review object based on user's info
        form = TripReviewForm(request.POST, request.FILES, instance=place)

        # Check if form is valid
        if form.is_valid():
            form.save()
            messages.info(request, "Trip Information Updates")

        else:
            return redirect('place_details', place_pk=place_primary_key)

    # If GET, req, show place and form info

    return render(request, 'travel_wishlist/place_details.html', {'place_info': place})


@login_required
def delete_place(request, place_primary_key):
    place = get_object_or_404(Place, pk=place_primary_key)

    if place.user == request.user:
        place.delete()

        # Redirect to the home page
        return redirect('place_list')
    else:
        return HttpResponseForbidden()
