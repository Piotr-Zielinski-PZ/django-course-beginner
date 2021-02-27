# all we do is we define the serializer and then we secify the fields that we want to accept in our serializer input
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):                                  # we create a simple serializer that accepts a name input and the we're going to add it to our API view
    """serializes a name field for testing our APIView"""                       # and then we're going to use it to test the post functionality of our API view
                                                                                # here we create a field (in this case called name) and this is value that can be passed into the request that will be validated by the serializer
    name = serializers.CharField(max_length=10)                                 # we create a character field (called name) on our serializers
