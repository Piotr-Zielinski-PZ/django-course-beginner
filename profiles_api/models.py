from django.db import models                                                    # created by default, modify to add user model profile
from django.contrib.auth.models import AbstractBaseUser                         # adding abstract made user
from django.contrib.auth.models import PermissionsMixin                         # adding permissions mixin
from django.contrib.auth.models import BaseUserManager                          # default manager module that comes with django
# these are standard base classes that we neet to use when overwriting or
# costumizing the default django module
from django.conf import settings                                                # this is used to retrieve settings from our settings.py

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
    REQUIRED_FIELDS = ['name']                                                   # is says that the email is required (from line above) just like name


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


class ProfileFeedItem(models.Model):                                            # this is going to be the model we use to allow users to
    """Profiles status update"""                                                # store status updates in the system so every time they create a new update it's
                                                                                # going to create a new profile feed item object and associate that object with
                                                                                # the user that created it
# the way we link models to other models in Django is
# we use what's called a foreign key when we use the foreign key field it sets up
# a foreign key relationship in the database to a remote model
# the benefit of doing this is that it allows us to ensure that the integrity
# of the database is maintained so we can never create a profile feed item for a
# user profile that doesn't exist

    user_profile = models.ForeignKey(                                           # the first argument of a foreign key
        settings.AUTH_USER_MODEL,                                               # field in models is the name of the model that is the remote model for this foreign key
        # it will retrieve the value
        # from the author user model setting in our settings.py file so if we ever
        # swap this auth user model to a different model then the relationships
        # will automatically be updated without us having to go through and manually change
        # it everywhere that we've referenced it in our models.py file
        on_delete=models.CASCADE
        # it tells Django or it
        # tells the database what to do if the remote field is deleted
        # database needs to know what happens if we remove a user profile what should
        # happen to the profile feed items that are associated with it and the way we
        # do that is by specifying on_delete
    )
    status_text = models.CharField(max_length=255)                              # it's used to contain the text of the feed update
    created_on = models.DateTimeField(auto_now_add=True)                        # every time we create a new feed item automatically add the date time stamp that the item was
                                                                                # created so we don't need to manually set this when we're creating the item it will
                                                                                # automatically be set to the current time because of this auto now add parameter
    def __str__(self):
        """Return the model as a string"""                                      # string representation of our model so that is
                                                                                # to tell Python what to do when we convert a model instance into a string
        return self.status_text
