from django.test import TestCase
from django.urls import reverse  # urls that we made to search for

from .models import Place  # test our db Place object


class TestHomePage(TestCase):

    def test_home_page_shows_empty_list_message_for_empty_database(self):
        # Turn the url place list to an actual url a request can be made to
        home_page_url = reverse('place_list')

        # Self it is "this" test case, and then have the "client" make a request to get the url page using the application server
        response = self.client.get(home_page_url)

        # Assert template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Assert if the response contains the "no places in wishlist..." message
        self.assertContains(response, 'You have no places in your wishlist')


class TestWishList(TestCase):
    # List's of test places from fixture folder of JSON data off different visited and non visited place
    fixtures = ['test_places']

    def test_wishlist_contains_not_visited_places(self):

        # Another way to combine get request and reverse method
        response = self.client.get(reverse('place_list'))

        # Assert template was used
        # Check if wishlist.html was rendered
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Check if response includes these places and are NOT VISITED YET, and so they will be on the wishlist homepage
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')

        # Making sure response DOES NOT CONTAIN these places in wishlist because they were visited
        self.assertNotContains(response, 'San Francisco')

        self.assertNotContains(response, 'Moab')


class TestNoPlacesVisited(TestCase):
    def test_visited_page_where_no_places_visited_message_is_present(self):

        # Place visited requests
        response = self.client.get(reverse('places_visited'))

        # Assert template was used
        # Check if visited.html was rendered
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')

        # Contains no visited place message based on my visited html page
        self.assertContains(response, 'You have no places visited!')


class TestVisitedPlaces(TestCase):
    fixtures = ['test_places']

    def test_visited_places_shown(self):

        # Another way to combine get request and reverse method
        response = self.client.get(reverse('places_visited'))

        # Assert template was used
        # Check if visited.html was rendered
        self.assertTemplateUsed(
            response, 'travel_wishlist/visited.html')

        # Check if response includes these places in visited page
        self.assertContains(response, 'Moab')
        self.assertContains(response, 'San Francisco')

        # Making sure response DOES NOT CONTAIN these places in visited because they are in  homepage, as these places are not visited yet (based on the test data)
        self.assertNotContains(response, 'Tokyo')

        self.assertNotContains(response, 'New York')


class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place(self):
        # Test dummy data
        new_place_data = {'name': 'Tokyo', 'visited': False}

        #  Follow = True, data is saved and redirected to homepage.
        # So 2 requests are technically made, and so we need to tell the  test to redirect to place list page after saving data with that newly added test data on there
        response = self.client.post(
            reverse('place_list'), new_place_data, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Response.context is a method that returns the value of that place, essentially the "payload" or in other words, data that is being sent through to html. "users_places" is from views.py, which is from the key pair value Place object
        response_places = response.context['users_places']

        self.assertEqual(1, len(response_places))  # Check only one place

        tokyo_from_response = response_places[0]  # The first place

        tokyo_from_database = Place.objects.get(name='Tokyo', visited=False)

        # Check if the response (data response from template) and the  data from db is equal to each other

        self.assertEqual(tokyo_from_database, tokyo_from_response)


class TestVisitPlace(TestCase):
    fixtures = ['test_places']

    # Testing the action where adding place to visit checkbox
    def test_visit_place_added(self):

        # Data to provide to the url req
        # The primary key for Tokyo based on the dummy data
        visit_place_url = reverse('place_was_visited', args=(1,))  # Tokyo

        response = self.client.post(visit_place_url, follow=True)

        # Make sure if you redirected to a different html page, teh assert template used knows this!
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Tokyo will be to visited, meaning it will be out of wishlist.html
        self.assertNotContains(response, 'Tokyo')

        # New York will still be in wishlist
        self.assertContains(response, 'New York')

        tokyo_from_db = Place.objects.get(pk=1)

        # Check of Tokyo from DB is visited
        self.assertTrue(tokyo_from_db.visited)

        # Non Existent place method

    def test_non_existent_place(self):

        #  Non existent primary key
        visit_nonexistent_place_url = reverse(
            'place_was_visited', args=(123456,))

        response = self.client.post(
            visit_nonexistent_place_url, follow=True)

        # The status code should be 404, which is a non existent code and we want to make sure that request statues matches with the test response code too.
        self.assertEqual(404, response.status_code)
