from django.test import TestCase, override_settings, Client
from django.core.urlresolvers import reverse

@override_settings(SECURE_SSL_REDIRECT=False)
class TestSiteMap(TestCase):

    def setUp(self):
        self.client = Client()
    def test_sitemap_using_template(self):
        """
        Check the template used to render sitemap page
        """
        response = self.client.get(reverse('sitemap'))
        self.assertTemplateUsed(response, 'destination_dog/sitemap.html')

