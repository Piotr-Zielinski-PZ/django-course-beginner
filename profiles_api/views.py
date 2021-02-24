from rest_framework.views import APIView                                         # we installed rest_framework.views module in our requirements.txt file
from rest_framework.response import Response                                    # Response object returns responses from APIView so when we call the APIView we expect the standard Response object to be returned


# now we create the APIView class:
# each view expects a function for the different HTTP requests that can be made
# for the view

class HelloApiView(APIView):                                                    # this creates class based on APIView class that django rest framework provides
    """Test API View"""                                                         # and it allows us to define the application logic for our endpoint that we're gonna assign to this view
                                                                                # the way it works is we define a URL which is our endpoint and we assing to this view and the django handles it
                                                                                # with calling the appropriate function in the view for http request that we make.
    def get(self, reques,format=None):                                          # GET FUNCTION - is typically used to retrive a list of object or a specific object, so whenever we make HTTP GET request to the URL
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

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})            # every function that we add to API view thet is HTTP function (get, post, patch, put, delete)
                                                                                # must return a Response() object which will then output as part of when the API is called
                                                                                # Response must contain dictionary or a list which will then output as API is called so it converts the response object to JSON
                                                                                # so it needs to be either a list or a dictionary
