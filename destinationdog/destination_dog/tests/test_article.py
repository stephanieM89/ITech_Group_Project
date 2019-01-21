from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from destination_dog.models import UserProfile, Article
from django.contrib.auth.hashers import make_password

@override_settings(SECURE_SSL_REDIRECT=False)
class TestArticle(TestCase):

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

        # Create an article
        user = User.objects.get(username='Anne')
        userprofile = user.userprofile
        article= Article.objects.create(title="MyArticle", image="articles/dog.jpg", article="content", date=2018-12-11,
                                        author=userprofile, slug="myarticle", is_dotm=False)
        article.save()
        self.client = Client()

    def test_does_article_slug_work(self):
        """
        Test that the article slug works
        """
        article = Article(title='how to feed my dog')
        article.save()
        self.assertEqual(article.slug, 'how-to-feed-my-dog')


    def test_article_using_template(self):
        """
        Check the template used to render article page
        """
        response = self.client.get(reverse('article'))
        self.assertTemplateUsed(response, 'destination_dog/article.html')

    def test_article_list_using_template(self):
        """
        Check the template used to render article list page
        """
        response = self.client.get(reverse('article_list'))
        self.assertTemplateUsed(response, 'destination_dog/article_list.html')

    def test_article_list_with_no_articles(self):
        """
        If no articles exist, an appropriate messsage should be displayed
        """
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles found.")
        self.assertQuerysetEqual(response.context['categories'],[])

    def get_article(self, name):
        """
        Check that article is present in the database
        """
        try:
            article = Article.objects.get(name=name)
        except Article.DoesNotExist:
            article = None
        return article