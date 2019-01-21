from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

@override_settings(SECURE_SSL_REDIRECT=False)
class TestAbout(TestCase):

    def setUp(self):
        self.client = Client()

    def test_about_using_template(self):
        """
        Check the template used to render about page
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response,'destination_dog/about.html')

    def test_about_contains_create_message(self):
        """
        Check if the about page is there, and it contains the specified message
        'DestinationDog will provide advice and guidance to prospective owners'
        """
        response = self.client.get(reverse('about'))
        self.assertIn(b'DestinationDog will provide advice and guidance to prospective owners', response.content)

