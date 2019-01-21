from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from datetime import datetime, date

class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='articles', default='') #For the top of the article page
    article = models.TextField()
    date = models.DateField(default=date.today)
    author = models.ForeignKey('UserProfile', related_name='article')
    slug = models.SlugField(unique=True)
    is_dotm = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Dotm(models.Model):
    dog = models.CharField(max_length=128)
    owner = models.ForeignKey('UserProfile', related_name='dotm')
    image = models.ImageField(upload_to='dotm')
    created_at = models.DateTimeField(default=datetime.now())
    winner = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Dog of The Month Entries'

    def __str__(self):
        return self.dog

class Dog(models.Model):
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='dogs')
    breed = models.CharField(max_length=128)
    gender = models.CharField(max_length=20)
    about_me = models.TextField()
    owner = models.ForeignKey('UserProfile', related_name="dog", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=128, unique=True, primary_key=True)
    serType = models.CharField(max_length=128, default='')
    location = models.CharField(max_length=128, default='')
    mondayTimes = models.CharField(max_length=128, default='')
    tuesdayTimes = models.CharField(max_length=128, default='')
    wednesdayTimes = models.CharField(max_length=128, default='')
    thursdayTimes = models.CharField(max_length=128, default='')
    fridayTimes = models.CharField(max_length=128, default='')
    saturdayTimes = models.CharField(max_length=128, default='')
    sundayTimes = models.CharField(max_length=128, default='')
    contact = models.CharField(max_length=128, default='')
    email = models.CharField(max_length=128, default='')
    description = models.CharField(max_length=128, default='')
    ratings = models.IntegerField(default=0)
    provider = models.ForeignKey('UserProfile', related_name='service', on_delete=models.CASCADE, default='')
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey('UserProfile', related_name="event", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default='')
    attendees = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    def __str__(self):
        return self.user.username




