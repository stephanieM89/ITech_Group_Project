from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Dog
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse


@override_settings(SECURE_SSL_REDIRECT=False)
class TestEvent(TestCase):

    def setUp(self):

        # Create a test user
        self.user = User.objects.create(username="user")
        self.user.first_name = "User"
        self.user.last.name = "Test"
        self.user.password = make_password("password")

        # Create a test user profile
        self.profile = UserProfile(user=self.user)
        self.user.userprofile.save()
        self.user.save()

        # Create an event
        user = User.objects.get(username='Anne')
        userprofile = user.userprofile

        dog = Dog.objects.create(name='Spot', picture='dogs/dog.jpg', breed='poodle', gender='female',
                                 about_me='just a dog',  owner=userprofile, slug='spot')

        dog.save()
        self.client = Client()

    def get_dog_name(self, name):
        """
        Check that dog exists
        """
        try:
            dog = Dog.objects.get(name=name)
        except Dog.DoesNotExist:
            dog = None
        return dog
