from django.db import models                                                    # created by default, modify to add user model profile
from django.contrib.auth.models import AbstractBaseUser                         # adding abstract made user
from django.contrib.auth.models import PermissionsMixin                         # adding permissions mixin
from django.contrib.auth.models import BaseUserManager                          # default manager module that comes with django
# these are standard base classes that we neet to use when overwriting or
# costumizing the default django module


class UserProfileManager(BaseUserManager):                                      # we create manager to let the django know how to work with custom made user model in django commandline tools (such as superuser command)
    """Manager for user profiles"""                                             # because we customized our user model we need to tell django how to interact with this user model in order to create users
                                                                                # the way the manager work is you secify some functions within the manager that can be used to manipulate the objects within the model that manager is for
    def create_user(self,email,name,password=None):                             # django CLI will use it when creating a users with a commandline tool; if we don't specify a password then it will be by default to None
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have a email address')

        email = self.normalize_email(email)                                     # setting email case-nonsensitive
        user = self.model(email=email,name=name)                                # it creates new model that manager is representing, self.model is set to the model that the manager is for and then it will create an object with email and the name
        user.set_password(password)                                             # the password must be encrypted
        user.save(using=self._db)                                               # to save the user in database

        return user


    def create_superuser(self,email,name,password):                             # function that allows django to create superuser account
        """Create and save a new super user with given details"""
        user = self.create_user(email,name,password)
        user.is_superuser = True                                                # it is automaticly created by the PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):                           # class based on AbstractMadeUser and PermissionsMixin so we get all
    """Database model for users in the system"""                                # the functionality from the django default user model which allows us to costumize to our needs
                                                                                # python standard for writing doc strings, it simply tells us what this class does
                                                                                # below we can define various fields that we wanna provide to our
    email = models.EmailField(max_length=255,unique=True)                       # it says that we want a email column on our UserProfile database table and we want that column to be
                                                                                # EmailField with max_length=255(charachters) and we want to make sure that this is unique in our system
                                                                                # so we don't allow two users to have the same email addres
    name = models.CharField(max_length=255)                                     # to store a name
    is_active = models.BooleanField(default=True)                               # to determine if a user's profile is activated or not (we set them activated by default) BooleanField is used to hold True or False value
    is_staff = models.BooleanField(default=False)                               # it determines if the user is a staff user (if user is permitted to acces django admin etc.)


# now we have to specify model manager that we're gonna use for the objects and
# this is required because we neet to use our custom user model (UserProfile)
# with django CLI, so django needs to have a custom model manager for the user
# model, so it knows how to create users and control users using django
# commandline tools


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'                                                    # overwriting a default username with previously created email, so when logging we neet to use email, not name
    REQUIRED_FIELD = ['name']                                                   # is says that the email is required (from line above) just like name


# next we will create functions which are used for django to interact with our
# custom user model

    def get_full_name(self):                                                    # we give django a ability to get user's full name
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name


# finally we neet to secify string representation of our model... this is a item
# thet we wanna return when we convert a UserProfile's object to a string

    def __str__(self):
        """Return string representation of our user"""
        return self.email                                                       # it is recommended for all django models
