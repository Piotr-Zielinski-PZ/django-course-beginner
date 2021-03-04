from rest_framework.views import APIView                                        # we installed rest_framework.views module in our requirements.txt file
from rest_framework.response import Response                                    # Response object returns responses from APIView so when we call the APIView we expect the standard Response object to be returned
from rest_framework import status                                               # the status object from rest framework is a list of handy HTTP codes that we can use when returning responses from our API... we use them in POST handler
from profiles_api import serializer                                             # serializers is the module that we created in our profiles API project... by this we're going to tell our API view what data to expect when making post, put and patch requests
from rest_framework import viewsets


# now we create the APIView class:
# each view expects a function for the different HTTP requests that can be made
# for the view

class HelloApiView(APIView):                                                    # this creates class based on APIView class that django rest framework provides
    """Test API View"""                                                         # and it allows us to define the application logic for our endpoint that we're gonna assign to this view
                                                                                # the way it works is we define a URL which is our endpoint and we assing to this view and the django handles it
                                                                                # with calling the appropriate function in the view for http request that we make.


    serializer_class = serializer.HelloSerializer                              # this configures our API view to have the serializer class that we created lately


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
            name = serializer.validated_data.get('name')                        # we want to retrive the name field from validated data
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


    serializer_class = serializer.HelloSerializer                               # we're adding the serializer class and we can use the same serializer that we created
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
            name = serializer.validated_data.get('name')                        # we retrieve the name field
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
