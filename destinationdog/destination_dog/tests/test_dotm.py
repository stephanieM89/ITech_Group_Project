from django.test import TestCase, Client, override_settings
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Dotm
from django.contrib.auth.hashers import make_password

@override_settings(SECURE_SSL_REDIRECT=False)
class TestDotm(TestCase):

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

        dotm = Dotm.objects.create(name='Spot', owner=userprofile, image='dogs/dog.jpg',
                                 created_at='2018-01-01 12:00', winner=False, likes=0)
        dotm.save()
        self.client = Client()

def test_dotm_using_template(self):
    """
    Check the template used to render dog of the month page
    """
    response = self.client.get(reverse('dotm'))
    self.assertTemplateUsed(response, 'destination_dog/dotm.html')

def test_dotm_hall_of_fame_using_template(self):
    """
    Check the template used to render hall of fame page
    """
    response = self.client.get(reverse('dotm_hall_of_fame'))
    self.assertTemplateUsed(response, 'destination_dog/dotm_hall_of_fame.html')

