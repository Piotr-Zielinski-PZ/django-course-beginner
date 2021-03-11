# all we do is we define the serializer and then we secify the fields that we want to accept in our serializer input
from rest_framework import serializers

from profiles_api import models                                                 # this allows us to access our user profile model that we previously created

class HelloSerializer(serializers.Serializer):                                  # we create a simple serializer that accepts a name input and the we're going to add it to our API view
    """serializes a name field for testing our APIView"""                       # and then we're going to use it to test the post functionality of our API view
                                                                                # here we create a field (in this case called name) and this is value that can be passed into the request that will be validated by the serializer
    name = serializers.CharField(max_length=10)                                 # we create a character field (called name) on our serializers

class UserProfileSerializer(serializers.ModelSerializer):                        # we use a meta class to configure the serializer to point to a specific model in our project
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile                                              # this sets our serializer up to point to our user profile model
        fields = ('id', 'email', 'name', 'password')                            # so this is the list of fields that we want to work with
        extra_kwargs = {                                                        # we want to make this password field write only
            'password': {                                                       # the keys of the dictionary are the fields that we want to add the custom configuration
                'write_only': True,
                'style': {'input_type': 'password'}                             # we are going to add two more key value pairs the first one is
            }                                                                   # going to be write_only and the value is going to be true so this
        }                                                                       # says when we create our password field from our model set it to write only
                                                                                # equals true that means you can only use it to create new objects or update
                                                                                # objects... you can't use it to retrieve objects so when you do a get you won't
                                                                                # see the password field included in that response
                                                                                # the second thing we're going to do is add a custom style to this and this is
                                                                                # just for the browsable api and what it does is it will set the field type to a
                                                                                # password field which means you won't be able to see the input as you're typing
                                                                                # it so you'll just see the dots

# whenever we create a new object with our user profile serializer
# it will validate the object or validate the fields provided to the serializer
# and then it will call this create function passing in the validated data

# what this function does is it will override the create function and
# call our create user function that we previously defined
    def create(self, validated_data):                                           # we overwrite the create function... by default the model serializer allows us
        """Create and return a new user"""                                      # to create simple objects in the database so it uses the default create function
                                                                                # of the object manager to create the object. We want to override this
                                                                                # functionality for this particular serializer so that it uses the "create
                                                                                # user function" instead of the "create function" the reason we do this is so
                                                                                # that the password gets created as a hash and not the clear text
        user = models.UserProfile.objects.create_user(                          # we pass in the appropriate fields from the validated data
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

# If a user updates their profile, the password
# field is stored in cleartext, and they are unable to login.
# This is because we need to override the default behaviour of
# Django REST Frameworks ModelSerializer to hash the users password when updating.
# Bug fix:
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
# Explanation:
# The default update logic for the Django REST Framework (DRF) ModelSerializer
# code will take whatever fields are provided (in our case: email, name, password)
# and pass them directly to the model.
# This is fine for the email and name fields, however the password field
# requires some additional logic to hash the password before saving the update.
# Therefore, we override the Django REST Framework's update() method to add this
# logic to check for the presence password in the validated_data which is passed
# from DRF when updating an object.
# If the field exists, we will "pop" (which means assign the value and remove
# from the dictionary) the password from the validated data and set it using
# set_password() (which saves the password as a hash).
# Once that's done, we use super().update() to pass the values to the existing
# DRF update() method, to handle updating the remaining fields.



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    # we're going to set our model serializer to our
    # profile feed item class

    class Meta:
        model = models.ProfileFeedItem

    # this sets our serializer or our model serializer
    # to our profile feed item model that we created in models.py

        fields = ('id','user_profile','status_text','created_on')               # we need to make these fields available through our serializer
        extra_kwargs = {'user_profile': {'read_only': True}}                    # we don't want one user to be able to
                                                                                # create a new profile feed item and assign that to another user
