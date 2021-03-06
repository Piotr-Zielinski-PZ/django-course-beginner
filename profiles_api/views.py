from rest_framework.views import APIView                                        # we installed rest_framework.views module in our requirements.txt file
from rest_framework.response import Response                                    # Response object returns responses from APIView so when we call the APIView we expect the standard Response object to be returned
from rest_framework import status                                               # the status object from rest framework is a list of handy HTTP codes that we can use when returning responses from our API... we use them in POST handler
from rest_framework import viewsets
from rest_framework import filters                                              # we can use it to add filtering to a view set by in the user profile view set below the permissions classes list
                                                                                # we add a new class variable called filter_backends

from rest_framework.authentication import TokenAuthentication                   # the token authentication is going to be the type of
                                                                                # authentication we use for users to authenticate themselves with our API it
                                                                                # works by generating a random token string when the user logs in and then
                                                                                # every request we make to their API that we need to authenticate we add this
                                                                                # token string to the request and that's effectively a password to check that
                                                                                # every request made is authenticated correctly

from rest_framework.authtoken.views import ObtainAuthToken                      # we're going to use token authentication it works by generating a token which is like a
                                                                                # random string when we log in and then every request we make to the API that
                                                                                # we wish to authenticate we include this token in the headers
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from profiles_api import serializers                                             # serializers is the module that we created in our profiles API project... by this we're going to tell our API view what data to expect when making post, put and patch requests
from profiles_api import models
from profiles_api import permissions


# now we create the APIView class:
# each view expects a function for the different HTTP requests that can be made
# for the view

class HelloApiView(APIView):                                                    # this creates class based on APIView class that django rest framework provides
    """Test API View"""                                                         # and it allows us to define the application logic for our endpoint that we're gonna assign to this view
                                                                                # the way it works is we define a URL which is our endpoint and we assing to this view and the django handles it
                                                                                # with calling the appropriate function in the view for http request that we make.


    serializer_class = serializers.HelloSerializer                              # this configures our API view to have the serializer class that we created lately


    def get(self, request,format=None):                                         # GET FUNCTION - is typically used to retrive a list of object or a specific object, so whenever we make HTTP GET request to the URL
        """Returns a list of APIView features"""                                # that it will be assigned to this API View, it will call the get function and it will execute the logic that we write in the get function
                                                                                # "request" argument is passed by django rest framework and contains details of the request being made to the API
                                                                                # "format" adds a formal suffix to the end of of the endpoint of the url
        # here we're gonna define a list the features of a APIView
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',    # these are the functions that we can add to our APIView to support a different HTTP requests
            'IS similar to the traditional django view',                        # this list demonstrates how the API view works in practise
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})        # every function that we add to API view thet is HTTP function (get, post, patch, put, delete)
                                                                                # must return a Response() object which will then output as part of when the API is called
                                                                                # Response must contain dictionary or a list which will then output as API is called so it converts the response object to JSON
                                                                                # so it needs to be either a list or a dictionary


    def post(self, request):                                                    # POST FUNCTION - here we're gonna retrive the serializer and pass in the data that was sent in the request
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)                   # the "self.serializer_class" is the function that comes with the API view that retrives the configured serializer class
                                                                                # for our view so it's the standard way to retrive the serializer class when working with serializers in a view
                                                                                # The second part assigns the data so when you make a post
                                                                                # request to our API view the data gets passed in as request dot data so it is
                                                                                # part of the request object that's passed to our post request we assign this data
                                                                                # to our serializer class and then we create a new variable for our serializer
                                                                                # class called serializer

                                                                                # IF INPUT IS VALID
        if serializer.is_valid():                                               # serializer validate the input... it ensures that the input s valid to the specification (in our case we're gonna be validatinf if the input is no longer than 10 characters)
            name = serializers.validated_data.get('name')                        # we want to retrive the name field from validated data
                                                                                # this way we can retrive any data that we define in serializer.py
            message = f'Hello {name}'                                           # we're going to create a
                                                                                # new message and this message we're just going to return a message from our API
                                                                                # that contains the name that was passed in the post request
            return Response({'message': message})                               # we return the massage as the response

                                                                                # IF INPUT IS NOT VALID
        else:                                                                   # if the input is not valid we're going to return a HTTP 400 bad request response
            return Response(
                serializer.errors,                                              # return a response where we're going to pass in the errors that were generated by the serializer
                status=status.HTTP_400_BAD_REQUEST                              # by default the response returns HTTP 200 okay request so we need to change this to a 400 bad request
            )

    def put(self, request,pk=None):                                             # PUT FUNCTION - defines a new method for handling HTTP put requests HTTP put is often used to update an object
        """Handle updating an object"""                                         # what we do is we make a request with HTTP put and it will update the entire object with what we've provided in the request
                                                                                # PK is to take the ID of the object to be updated with the put request
        return Response({'method':'PUT'})                                       # we'll just return a dictionary with method and then the method that we made which is put so this
                                                                                # is where we would put any logic that we wanted to do whenever we did a HTTP put request to the API

    def patch(self, request, pk=None):                                          # PATCH FUNCTION - is used to do an update but only update the fields that were provided in the request
        """Handle a partial update of an object"""                              # so if you had a first name and a last name field and you made a patch request with just providing
                                                                                # the last name it would only update the last name
        return Response({'method': "PATCH"})

# DIFFERENCES BETWEEN HTTP PUT AND PATCH:
# if you had a first name and a last name field and you made a patch request
# with just providing the last name it would only update the last name whereas
# if you did a put request and you only provided the last name then in that
# case it would remove the first name completely because HTTP put is essentially
# replacing an object with the object that was provided whereas patch is only
# updated the fields that were provided in the request

    def delete(self, request, pk=None):                                         # DELETE FUNCTION - used for deleting objects in the database
        """Delete object"""
        return Response({'method': 'DELETE'})







class HelloViewSet(viewsets.ViewSet):                                           # functions that we add to a view set are a little bit different from the functions we've added to an API view
    """Test API ViewSet"""                                                      # for a view set we add functions that represent actions that we would perform on a typical API


    serializer_class = serializers.HelloSerializer                               # we're adding the serializer class and we can use the same serializer that we created
                                                                                # for our API view with the name field we can share the same serializer for both
                                                                                # of our view sets and we specify the serializer in our view set the same way as we do for our API view


    def list(self, request):                                                    # LIST FUNCTION - typically a HTTP GET to the root of the endpoint linked
        """Return a hello message"""                                            # to our view set; so it lists a set of objects that the view set represents
        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)                   # we pass in the data that was made in the request and we passed that
                                                                                # in as the data attribute of our serializer which we retrieve using the serializer class
        if serializer.is_valid():
            name = serializers.validated_data.get('name')                        # we retrieve the name field
            message = f'hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve (self, request, pk=None):                                      # RETIVE FUNCTION - is for retrieving a specific object in our view
        """Handle getting an object by its ID"""                                # set so you would typically pass in a primary key ID to the URL in
                                                                                # the request and that will return or retrieve the object with that primary key ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):                                         # UPDATE FUNCTION - maps to a HTTP put on the primary key item of our view set
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response ({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):                                        # if you wish to remove an object then you would call HTTP delete
        """Handle removing an object"""                                         # on our view set which would then call this destroy function and run the
        return Response({'http_method': 'DELETE'})




# rest framework browsable API knows that our
# view set is going to accept a post with a name because we assigned the
# serializer class to the top of our view set and it looks at the serializer and
# it determines which fields we're going to accept in the request that we
# make to the api and it provides them here for us in the handy browsable api view


# unlike the API view we don't actually see the put patch and delete
# methods here on the hello view set API that's because view sets expect that we
# will use this endpoint to retrieve a list of objects in the database and we
# will specify a primary key ID in the URL when making changes to a specific object
# so if we want to see these additional functions that we added we need to add
# something to the end of the URL... now in this case, because we aren't actually
# retrieving any real objects it doesn't matter what we type but if we just put
# a number there that would represent a primary key of an object that we wanted to
# change and hit enter then it will change the page to the get request which is the
# retrieve of that object so when we specify a primary key to a view set URL
# it calls the retrieve function and as we can see in our retrieve function

# if you want to do a partial update then you need to click on the raw data tab here and then
# you can see you get the put and patch options if you click on patch it returns
# the HTTP method patch and that's because that's what we returned from our partial
# update function that we defined


class UserProfileViewSet(viewsets.ModelViewSet):                                # the model view set is very similar to a standard view set
    """Handle creating and updating profiles"""                                 # except it's specifically designed for managing models through
                                                                                # our API so it has a lot of the functionality that we
                                                                                # need for managing models built into it
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()                                 # we're provideing the query set then Django rest framework can figure out the name from the model that's assigned to it

# the way we use a model view set is we connect it up to a
# serializer class just like we would a regular view set and you provide a query
# set to the model view set so it knows which objects in the database are going
# to be managed through this view set

    authentication_classes = (TokenAuthentication,)                             # we can configure one or more types of
                                                                                # authentication with a particular view set in the Django rest framework the way
                                                                                # it works is we just add all the authentication classes to this
                                                                                # authentication classes class variable

    permission_classes = (permissions.UpdateOwnProfile,)

# the authentication class is set how the user will authenticate
# the permission classes is set how the user
# gets permission to do certain things

# every request that gets made it gets passed through our permissions.py file
# and it checks "has-object-permissions" function to see whether the
# user has permissions to perform the action they're trying to perform

    filter_backends = (filters.SearchFilter,)                                   # it will add a filter back end and we can add one or more filter back ends to a particular
    search_fields = ('name', 'email',)                                          # view set we're going to add a filter back end for the search filter
                                                                                # then we'll specify the search fields name and email this will mean that the Django rest framework will
                                                                                # allow us to search for items in this view set by the name or email field

class UserLoginApiView(ObtainAuthToken):
    """Handling creating user authentication tokens"""

# obtain auth token class that is provided by the Django rest framework
# is really handy and we could just add it
# directly to a URL in the URLs.py file however it doesn't by default
# enable itself in the browsable Django admin site so we need to override this
# class and customize it so it's visible in the browsable api so it makes it
# easier for us to test so what we need to do is add a class variable here:

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES                    # it adds the renderer classes to our obtain auth token view
                                                                                # which will enable it in the Django admin


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatud,                                            # this will make sure that a
        IsAuthenticated                                                         # user must be authenticated to perform any request that is not a read request
    )                                                                           # so that will get rid of the issue of users trying to create a new feed item
                                                                                # when they're not authenticated
                                                                                # on top of that we'll also ensure that users can
                                                                                # only update statuses where the user profile is assigned to their user which
                                                                                # will stop users being able to update the statuses of other users in the system

    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""

        # the perform create function is a handy feature of the Django rest framework that allows you to
        # override the behavior or customize the behavior for creating objects through a
        # Model View set so when a request gets made to our view set it gets passed into
        # our serializer class and validated

        serializer.save(user_profile=self.request.user)                         # when a new object is created Django
                                                                                # rest framework calls perform create and it passes in the serializer that we're
                                                                                # using to create the object
