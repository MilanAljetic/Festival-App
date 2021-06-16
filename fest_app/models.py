from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.gis.db import models
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(gettext_lazy('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Manager(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(gettext_lazy('email address'), unique=True)
    user_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('user_name',)

    def __str__(self):
        return self.user_name

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
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Featured image', blank=True)
    description = models.TextField()
    create_event_time = models.DateTimeField(auto_now=True)
    upload_event_time = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name_plural = 'Festivals'
        ordering = ('-create_event_time',)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Festival, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('fest_app:festival_detail', args=[self.slug])

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
