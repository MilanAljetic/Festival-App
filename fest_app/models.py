from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class State(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city



class Festival(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=200)
    start_date = models.DateTimeField(auto_now=False)
    finish_date = models.DateTimeField(auto_now=False)
    country = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Featured image', blank=True)
    description = models.TextField()
    create_event_time = models.DateTimeField(auto_now=True)
    upload_event_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Festivals'
        ordering = ('-create_event_time',)

    def __str__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    application_time = models.DateTimeField(auto_now=True)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.email
