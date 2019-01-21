import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','destinationdog.settings')

django.setup()

from django.contrib.auth.models import User
from destination_dog.models import Article, UserProfile, Dotm
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta, timezone

def populate_articles():

    print("Populating articles...")
    user = User.objects.get(username="kayleighchisholm")
    profile = user.userprofile

    articles = [
        {
            "title": "Dog Stuff",
            "image": "articles/dog.jpg",
            "article":"Article Content",
            "date":'2018-03-25',
            "author": profile,
            "slug": "dog-stuff",
        },
        {
            "title": "More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "date": '2017-03-25',
            "author": profile,
            "slug": "more-dog-stuff",
        },
        {
            "title": "Even More Dog Stuff",
            "image": "articles/dog.jpg",
            "article": "Article Content",
            "date": '2018-01-25',
            "author": profile,
            "slug": "even-more-dog-stuff",
        }
    ]

    for data in articles:

            a = Article()
            a.title = data['title']
            a.image = data['image']
            a.article = data['article']
            a.date = data['date']
            a.author = data['author']
            a.slug = data['slug']
            a.save()

def populate_users():
    print("Populating users...")

    users = [
        {
            "username": "kayleighchisholm",
            "first_name": "Kayleigh ",
            "last_name": "Chisholm",
            "password": make_password("destinationdog"),
        },
        {
            "username": "kellymcdonald",
            "first_name": "Kelly",
            "last_name": "McDonald",
            "password": make_password("destinationdog"),
        },
        {
            "username": "stephanieman",
            "first_name": "Stephanie",
            "last_name": "Man",
            "password": make_password("destinationdog"),
        },
    ]

    for data in users:

        u = User.objects.get_or_create(username=data['username'])[0]
        u.first_name = data['first_name']
        u.last_name = data['last_name']
        u.password = data['password']
        u.save()

        profile = UserProfile(
            user=User.objects.get(username=data['username']),
            picture="profile_images/profile.png"
        )
        profile.save()

def populate_dotm():

    print("Populating Dog of the Month Entries...")
    user = User.objects.get(username="kayleighchisholm")
    profile = user.userprofile

    user2 = User.objects.get(username="kellymcdonald")
    profile2 = user2.userprofile

    user3 = User.objects.get(username="stephanieman")
    profile3 = user3.userprofile


    dotm = [

        {
            "dog": "Alfie",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc),
            "winner": False

        },
        {
            "dog": "Gizmo",
            "image": "articles/dog.jpg",
            "owner": profile2,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=5),
            "winner": False

        },
        {
            "dog": "Pablo",
            "image": "articles/dog.jpg",
            "owner": profile3,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=50),
            "winner": False
        },
        {
            "dog": "January",
            "image": "articles/dog.jpg",
            "owner": profile2,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=434),
            "winner": True
        },
        {
            "dog": "February",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=403),
            "winner": True
        },
        {
            "dog": "March",
            "image": "articles/dog.jpg",
            "owner": profile3,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=372),
            "winner": True
        },
        {
            "dog": "April",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=341),
            "winner": True
        },
        {
            "dog": "May",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=310),
            "winner": True
        },
        {
            "dog": "June",
            "image": "articles/dog.jpg",
            "owner": profile2,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=279),
            "winner": True
        },
        {
            "dog": "July",
            "image": "articles/dog.jpg",
            "owner": profile3,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=248),
            "winner": True
        },
        {
            "dog": "August",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=217),
            "winner": True
        },
        {
            "dog": "September",
            "image": "articles/dog.jpg",
            "owner": profile3,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=186),
            "winner": True
        },
        {
            "dog": "October",
            "image": "articles/dog.jpg",
            "owner": profile2,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=155),
            "winner": True
        },
        {
            "dog": "November",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=124),
            "winner": True
        },
        {
            "dog": "December",
            "image": "articles/dog.jpg",
            "owner": profile3,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=93),
            "winner": True
        },
        {
            "dog": "January",
            "image": "articles/dog.jpg",
            "owner": profile2,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=62),
            "winner": True
        },
        {
            "dog": "February",
            "image": "articles/dog.jpg",
            "owner": profile,
            "created_at": datetime.now(tz=timezone.utc) - timedelta(days=31),
            "winner": True
        },
    ]

    for data in dotm:
        d = Dotm()
        d.dog = data['dog']
        d.image = data['image']
        d.owner = data['owner']
        d.created_at = data["created_at"]
        d.winner = data['winner']
        d.save()





    # Start execution here!
if __name__ == '__main__':

    print("Starting Rango population script...")
    populate_users()
    populate_articles()
    populate_dotm()
