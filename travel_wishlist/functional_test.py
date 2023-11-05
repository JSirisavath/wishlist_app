from selenium.webdriver.chrome.webdriver import WebDriver

from django.test import LiveServerTestCase


class TitleTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        # Need to wait for browser page to load and then have code run after 10 seconds
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Travel Wishlist', self.selenium.title)


class AddPlacesTest(LiveServerTestCase):
    fixtures = ['test_places']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        # Need to wait for browser page to load and then have code run after 10 seconds
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_new_place(self):

        # selenium is practically your testing browser, and how we test each component within the browser is by targeting that element based on their id name. We can essentially "manipulate" the html components and use them for tests and or send data
        self.selenium.get(self.live_server_url)


# Error functional_test.py", line 44, in test_add_new_place
#     input_name = self.selenium.find_element_by_id('id_name')
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'

        input_name = self.selenium.find_element_by_id('id_name')

        input_name.send_keys('Denver')

        add_button = self.selenium.find_element_by_id('add-new-place')

        add_button.click()  # Basically submit the add-button with data

        # The pk after the dummy test place, and since the pk are auto increment, the next is 5
        denver = self.selenium.find_element_by_id('place-name-5')

        # Checking if the word Denver matches with the text denver value element from the html
        self.assertEqual('Denver', denver.text)

        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)
