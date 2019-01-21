
from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

@override_settings(SECURE_SSL_REDIRECT=False)
class TestAbout(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contact_us_using_template(self):
        """
        Check the template used to render contact us page
        """
        response = self.client.get(reverse('contactus'))
        self.assertTemplateUsed(response, 'destination_dog/contactus.html')

