from django.test import TestCase, Client, override_settings
from django.urls import reverse


@override_settings(SECURE_SSL_REDIRECT=False)
class TestIndex(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_using_template(self):
        """
        Check the template used to render home page
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'destination_dog/home.html')

    def test_index_contains_message(self):
        """
        Check if there is the message 'all about the destination'
        """
        response = self.client.get(reverse('home'))
        self.assertIn(b'all about the destination', response.content)

    def test_index_has_title(self):
        """
        Check to make sure that the title tag has been used and
        template contains html
        """
        response = self.client.get(reverse('home'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title', response.content)

