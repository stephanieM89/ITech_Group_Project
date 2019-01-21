from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse

@override_settings(SECURE_SSL_REDIRECT=False)
class TestForum(TestCase):

    def setUp(self):
        self.client = Client()

    def test_forum_using_template(self):
        """
        Check the template used to render forum page
        """
        response = self.client.get(reverse('forum'))
        self.assertTemplateUsed(response, 'destination_dog/forum.html')
