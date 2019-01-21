from django.test import TestCase, Client, override_settings
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Event
from django.contrib.auth.hashers import make_password


@override_settings(SECURE_SSL_REDIRECT=False)
class TestEvent(TestCase):

    def setUp(self):

        # Create a test user
        self.user = User.objects.create(username="user")
        self.user.first_name = "User"
        self.user.last.name = "Test"
        self.user.password = make_password("password")

        # Create a test user profile
        self.user.userprofile = UserProfile(user=self.user)
        self.user.userprofile.save()
        self.user.save()

        # Create an event
        user = User.objects.get(username='Anne')
        userprofile = user.userprofile

        event = Event.objects.get_or_create(name='Walk', description='Take a walk in the park.', location='Park',
                                            date='2018-05-05', time='12:00', user=userprofile, slug='walk',
                                            attendees=0)
        event.save()
        self.client = Client()

    def test_show_event_using_template(self):
        """
        Check the template used to render events page
        """
        response = self.client.get(reverse('show_event'))
        self.assertTemplateUsed(response, 'destination_dog/event.html')

    def test_does_event_slug_work(self):
        event = Event(name ='walk in the park')
        event.save()
        self.assertEqual(event.slug, 'walk-in-the-park')

    def get_event(self, name):
        """
        Check that event exists
        """
        try:
            event = Event.objects.get(name=name)
        except Event.DoesNotExist:
            event = None
        return event

