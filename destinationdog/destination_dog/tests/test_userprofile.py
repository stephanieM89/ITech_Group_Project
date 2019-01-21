from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from destination_dog.models import UserProfile

@override_settings(SECURE_SSL_REDIRECT=False)
class TestUserAccount(TestCase):

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

        self.client = Client()

    def test_user_account_profile(self):

        self.client.login(username="user", password="password")
        response = self.client.get(reverse('user_profile'))

        """
        Checks profile picture
        """
        self.assertContains(response, '<img src="/media/profile_images/',
                            msg_prefix="User account contains profile image")
        """
        Checks log out button 
        """
        self.assertContains(response, '<a href="/logout/">Logout</a>',
                            msg_prefix="User account contains logout button")
