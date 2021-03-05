from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):                             # this is a base permission class that Django rest framework
    """Allow users to edit their own profile"""                                 # provides for making our own custom permissions classes

# the way we define permission classes is we add a has
# object permissions function to the class which gets called every time a request
# is made to the API that we assign our permission to
# this function will return a true or a false to determine whether the authenticated user
# has the permission to do the change they're trying to do

    def has_object_permission(self, request, view, obj):                        # every time a request is made the Django rest
        """Chacek user that's trying to edit their own profile"""               # framework will call this function has object permission and it will pass in
                                                                                # the request object the view and the actual object that we're checking the
                                                                                # permissions against
# we need to check whether we should allow or deny this change and add the rules in here
# we're going to check the method that is being made for the request and we're going to see
# whether that is in the safe methods list
# the method is the HTTP method that is
# being used on the current request so that could be a HTTP GET put patch or delete request
# The safe methods are methods that don't require or don't make
# any changes to the object so a safe method would be for example HTTP GET
# because all we're doing is we're reading an object
# we want to allow users to view other users profiles but only be able to make
# changes to their own profile we do this by writing:

        if request.method in permissions.SAFE_METHODS:                          # if the method that's being used is a HTTP GET then it will be in the safe methods
            return True                                                         # therefore it will just return true and allow the request

# What we're going to do is we're going to check whether the object they're updating matches their
# authenticated user profile that is added to the authentication of the request so
# when we authenticate a request it will assign the
# authenticated user profile to the request and we can use this to compare
# it to the object that is being updated and make sure they have the same ID
# we do this by typing:

        return obj.id == request.user.id 
