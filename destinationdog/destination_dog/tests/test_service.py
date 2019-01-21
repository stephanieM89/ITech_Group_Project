from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Service
from django.contrib.auth.hashers import make_password


@override_settings(SECURE_SSL_REDIRECT=False)
class TestService(TestCase):

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

        # Create a service
        user = User.objects.get(username='Anne')
        userprofile = user.userprofile

        service = Service.objects.get_or_create(serType='Vets', name='SuperVet', location='Glasgow', mondayTimes='9 to 5',
                                                tuesdayTimes='9 to 5', wednesdayTimes='9 to 5', thursdayTimes='9 to 5',
                                                fridayTimes='9 to 5', saturdayTimes='9 to 5', sundayTimes='9 to 5',
                                                contact = '01410000000', email='destinationdog@email.com',
                                                description='Best vets', ratings= 3, provider=userprofile, slug='supervet')
        service.save()
        self.client = Client()

    def test_get_service(self, name):
        """
        Check that service exists
        """
        try:
            service = Service.objects.get(name=name)
        except Service.DoesNotExist:
            service = None
        return service

    def test_service_with_name(self):
        """
        Check that there is a service called Vets
        """
        service = self.get_service('Vets')
        self.assertIsNotNone(service)

    def test_does_service_slug_work(self):
        service = Service(name='Super Vet')
        service.save()
        self.assertEqual(service.slug, 'super-vet')

    def test_locate_service_using_template(self):
        """
        Check the template used to render locate services page
        """
        response = self.client.get(reverse('locateservice'))
        self.assertTemplateUsed(response, 'destination_dog/locateservice.html')

    def test_show_service_using_template(self):
        """
        Check the template used to render show service page
        """
        response = self.client.get(reverse('service'))
        self.assertTemplateUsed(response, 'destination_dog/service.html')

