# Table of Contents

1. Creating a git local project.
2. Pushing project to GitHub.
3. Creating Vagrant file.
4. Set up Vagrant box.
5. Run and contact to the server.
6. Create Python Virtual Environment.
7. Install required Python packages.
8. Create a new Django project & app.
9. Enable app in the Django.
10. Test and commit changes.
11. Django models.
12. Create a user database model.
13. Add a user model manager.
14. Set user custom model.
15. Create Django migration file and sync DB.
16. Create a superuser.
17. Enable Django Admin.
18. Test Django Admin.
19. APIViews.
20. Create first APIView.
21. Configure view URL.
22. Create a serializer.
23. Add POST method to APIView.
24. Add PUT, PATCH and DELETE methods in APIView.
25. ViewSets.
26. Create a simple ViewSet.
27. Add URL Router.
28. Add create, retrieve, update, partial_update and destroy functions.
29. Test ViewSet.
30. Plan our profile API.
31. Create user profile serializer.
32. Create profiles ViewSet.
33. Register profile Viewset with the URL router - to access it from the browser.
34. Create permission class.
35. Add authentication and permissions to ViewSet.
36. Add search profiles feature.
37. Create login API ViewSet.
38. Set token header using ModHeader extension.
39. Plan profile feed API.
40. Add new model item.
41. Create and run model migration.
42. Add profile feed model to admin.
43. Create ProfileFeedItem serializer.
44. Create ViewSet for our profile feed item.
45. Add permissions for feed API.
46. Restrict viewing status updates to logged in users only.
47. Add SSH key pair to AWS.
48. Create EC2 server instance.
49. Add deployment script and configs to our project.
50. SSH to our server and deploy to server.
51. Update allowed hosts and deploy changes.

# Creating a git local project

1. Make wanted folder a project folder by adding it in Atom as project file.
2. Using terminal go to your project folder and type *git init* to initialize
   local git project.
3. Add __profiles_rest_api/README.md__ file to the project.
4. Add __profiles_rest_api/.gitignore__ file to tell your project to do not add
   files or directories written in it while doing *git commit*.
5. Add license to the project.
6. Type *git add .* to add newly created files to the local git project.
7. Type *git commit -am "__note__"* to update local git project.

# Pushing project to GitHub

1. Create public/private key; in terminal:
   * *ls ~/.ssh* - check if there is no ssh file in the project directory,
   * *ssh-keygen -t rsa -b 4096 -C "__email address__"* - determine parameters
     of the key,
   * input id for the key,
   * input pass phrase for the key.
2. Type *cat ~/.ssh/id_rsa.pub* in terminal.
3. Copy outputted key (everything).
4. Add ssh key to account by naming it and pasting copied key to the GitHub account.
5. Create new public repository with the new name.
6. In terminal run few lines of code suggested by GitHub to **push an existing repository**.

![Git Data Transport Commands](https://user-images.githubusercontent.com/69716167/104955042-ceeeff00-59c9-11eb-831a-04cf95420581.png)

# Creating Vagrant file

(to have local development server that we can use to run and test API)

1. Type *vagrant init ubuntu/bionic64* to initialize the project with vagrant file
   and it bases it on Ubuntu bionic64 base image.

# Set up Vagrant box

1. By editing __profiles_rest_api/Vagrantfile__ customize development server.
2. Set system, version, network, add Python to the machine.

# Run and contact to the server

1. Run *vagrant up* in the terminal (VirtualBox needed) to start virtual machine.
2. Run *vagrant ssh* to connect to the server by ssh protocol.
3. To access project files go to Vagrant directory on virtual machine by typing
   *cd /vagrant* in terminal while connected to the server.
4. We can add Python program to the project and run it on vm by typing
   *python __file_name.py__*.

# Create Python Virtual Environment

1. To create Python environment type in terminal *python -m venv ~/env* while
   logged to vm.
2. Activate Python virtual environment by typing *source ~/env/bin/activate*.
3. To switch off the environment just type *deactivate*.

# Install required Python packages

1. Create __profiles_rest_api/requirements.txt__ file in your project where you
   will add packages' names and their versions.

Note: It is a good practice to set static version of the program to avoid unexpected
      updates that can be incompatible for other packages.

2. While in */vagrant* file and Python virtual environment activated, type
   *pip install -r __file_with_previously_added_packages.txt__*.

# Create a new Django project & app

1. Make sure that you are still in terminal with virtual environment activated and
   with directory set to */vagrant*.
2. To start a new project with a specific name in a specific location type
   *django-admin.py startproject __name_of_the_project__ .* while "." is the
   root location of the project.

Note: If "." will not be passed there will be created a sub folder with the name
      passed in the __name_of_the_project__ argument.

3. To create Django app within our project for our Profiles API type
   *python manage.py startapp profiles_api*. This will create a new file with our app.

Note: Django can consist of one or more sub applications within a project that you can
      use to separate different functionality within your project.

# Enable app in the Django

1. Open __profiles_project/settings.py__ in Atom.
2. Add *"rest_framework"*, *"rest_framework.authtoken"* and *"profiles_api"* to
   *INSTALLED_APPS* list.

Note: *"rest_framework"* - app for Django REST Framework,
      *"rest_framework.authtoken"* - allows to use authentication token functionality.

# Test and commit changes

1. To start Django Web Development Server type in terminal (activate PVE and
   set to __/vagrant__ directory) *python manage.py runserver 0.0.0.0:8000*,

Note: *python manage.py runserver 0.0.0.0:8000* means that we run
      Django Web Development Server on every available network adapter (0.0.0.0)
      on port 8000 (port must match with settings in __profiles_rest_api/Vagrantfile__).
      Now the server is running and we can check it by going to our browser and
      browsing __127.0.0.1:8000__.

# Django models

In Django we use models to describe the data we need for our application. Django
then uses these models to set up and configure our database to store our data effectively.

Each model in Django maps to a specific table within our database. Django handles
the relationship between our models and the database for us so we never need
to write any SQL statements or interact with the database directly.

# Create a user database model

1. Create user profile model (Django by default can create user model but we
   will override it and create our custom profile model).
2. Best practice is to keep all of the models files (all of the database models)
   in a file called __profiles_api/models.py__ within our app.
3. In __profiles_api/models.py__ import *from django.contrib.auth.models import AbstractBaseUser*
   and *from django.contrib.auth.models import PermissionsMixin* as they are standard
   base classes that you need to use when overriding or customizing the default
   Django user model.
4. Create new class for models (*__go to profiles_api/models.py for more informations__*).

# Add a user model manager

Note: Because we have customized our user model we need to tell Django how to
      interact with this user model in order to create users because by default
      when it creates a user it expects a username field and a password field but
      we have replaced the username field with a email field so we just need to
      create a custom manager that can handle creating users with an email fields
      instead of a username field.

1. Create custom user manager in __profiles_api/models.py__
   (*__for details go to profiles_api/models.py__*).

Note: The way manager work is you specify some functions within the manager
      that can be used to manipulate objects within the model that the manager is for.

# Set user custom model

Note: Now that we have set custom user model and custom user model manager we
      can configure our project to use these as the default user model.

1. Go to __profiles_project/settings.py__ to the bottom of the file.
2. Type *AUTH_USER_MODEL = '__string that represents the model that we want to use as the Django user model__'*.

# Create Django migration file and sync DB

Note: Migration files are used for models that we have added to the project.
      The way that Django manages the database is it creates what is called a
      migration file that stores all of the steps required to make our database
      match our Django models. Every time we change a model or add additional
      models to our project we need to create a new migration file. The migration
      file will contain the steps required to modify the database to match our
      updated models. So for example if we add a new model to our project then we
      need to be able to create a new table in the database and the way that Django
      does this is it uses what is called migrations.

1. To create Django migrations use the Django command-line tool. Open up the
   terminal and type:
    * *cd __location of Vagrant machine__* - to define which Vagrant machine will be used,
    * *vagrant up* - to start up machine,
    * *vagrant ssh* - to connect to the machine by ssh protocol,
    * *cd /Vagrant*,
    * *source ~/env/bin/activate* - to activate virtual environment,
    * *python manage.py makemigrations __name of the app we want to make migrations for - profiles_api__* -
      to create new migration file for user profiles model,
    * *python manage.py migrate* - run migrations (will make all the changes required
      to set up our database for our Django project).

# Create a superuser

1. To create superuser open up the terminal.
2. With virtual environment activated type *python manage.py createsuperuser*.
3. Follow the instructions given by terminal.

# Enable Django Admin

Note: To enable admin and look up for more informations go to __profiles_api/admin.py__.

# Test Django Admin

1. Start development server by typing *python manage.py runserver 0.0.0.0:8000*.
2. Open up browser and search *127.0.0.1:8000/admin* to launch development website
   with admin enabled.
3. Log in using previously created account of superuser.

Note: Three sections will appear (representing three different apps in our project):
        * __AUTH TOKEN__ - automatically added as part of Django REST framework
          when we enabled our tokens,
        * __AUTHENTICATION AND AUTHORIZATION__ - part of Django. This and __AUTH TOKEN__
          allows authentication system,
        * __PROFILES_API__ - created by us. we can see that the model we created
          is right below named *User profiles*. Notice that it is the name Django
          got from the name we have given to the user profile class in __profiles_api/models.py__
          (Django separates camel casing [capital letters] and adds letter "s"
          at the end - this is because it is normalized to call classes singular
          with camel casing).

# APIViews

The Django REST framework offers a couple of helper classes we can use to create
our API endpoints: the __APIView__ and the __ViewSet__. Both classes are
slightly different and offer their own benefits.

The __APIView__ is the most basic type of view we can use to build our API.
It enables us to describe the logic which makes our API endpoint. An __APIView__
allows us to define functions that match the standard HTTP methods:
  * *get* - return one or more items,
  * *post* - create an item,
  * *put* - update an item,
  * *patch* - partially update an item,
  * *delete* - delete an item.
__Every HTTP method must return response.__
By allowing us to customize the function for each HTTP method on our API URL,
__APIViews__ give us the most control over our application logic. This is perfect
in cases where you need to do something a little bit different from simply updating
objects in the database such as:
  * calling other APIs,
  * working with local files.
When to use __APIViews__:
  * need full control over your application logic (when you are running a very
    complicated algorithm or updating multiple data sources in one API call),
  * processing files and rendering a synchronous response (when you are validating
    a file and returning the result in the same call),
  * calling other APIs/services in the same request,
  * access local files or data.

# Create first APIView

Note: Open __profiles_api/viws.py__ for more informations.

# Configure view URL

Note: The way that Django URLs work is that we have the __profiles_project/urls.py__
that is the entry point for all of the URLs in our app. We store every URL in
*urlpatterns* list.

1. We have to create a new __urls.py__ for __profiles_api__ app.
2. Import *include* from *django.urls* in __profiles_project/urls.py__.
3. Add new URL to *urlpatterns* (*'api/'*), call *include* and pass in the name
   of the app and the module we want to include that contains our URLs (*'profiles_api.urls'*).
4. Next go to __urls.py__ in __profiles_api__ and import *path* from *django.urls*
   and *views* from *profiles_api*.
5. Create a new variable or a list variable called *urlpatterns* where we will store
   paths that map to views in our project (more informations - go to __profiles_api/urls.py__).

# Create a serializer

1. Create a new file at __profiles_api__ and call it __serializers.py__
   (for more informations go to __profiles_api/serializers.py__).

# Add POST method to APIView

1. Import *status* and *serializers* to __profiles_api/views.py__.
2. Add *post* class method and add logic to it (more informations in __views.py__).
3. Test the results on web page.

# Add PUT, PATCH and DELETE methods in APIView

1. Go to __profiles_api/views.py__ for more informations.

Note: The difference between PUT and PATCH is that the PUT method updates the
      whole object while PATCH only does this partially. So for example if we
      change the name and the id for our object and we will use PUT method we
      will be able to update both name and id. But if we use PATCH method we will
      be able to update name or id.

2. Test the results on website. Remember that PATCH method is more complex but
   still quite similar to the PUT so you will find it in PUT area but in __Raw data__
   overlap.

# ViewSets

Just like __APIViews__, __ViewSets__ allow us to write the logic for our endpoints. However
instead of defining functions which map to HTTP methods, __ViewSets__ accept functions
that map to common API object actions such as:
  * *list* - for getting a list of objects,
  * *create* - for creating new objects,
  * *retrieve* - for getting a specific object,
  * *update* - for updating an object,
  * *partial_update* - for updating part of an object,
  * *destroy* - for deleting an object.
Additionally __ViewSets__ can take care a lot of the common logic for us.
They are perfect for writing APIs that perform standard database operations
and they are the fastest way to make an API which interfaces with a database back-end.
When to use __ViewSets__ rather than __APIViews__:
  * if you need to write an API that performs a simple create, read, update
    and delete operations (CRUD) on an existing database model,
  * if you need a quick and simple API,
  * if you need little or no customization on the logic,
  * if your API is working with standard database structure.

# Create a simple ViewSet

1. Head over to __profiles_api/views.py__.
2. Import *viewsets* from *rest_framework*.
3. Create a new *HelloViewSet* class and add functions to it.

Note: __ViewSet's__ methods are different from the __APIView's__. While __APIView's__
      methods concentrate for particular HTTP methods that you want to support
      on your endpoint, __ViewSet's__ methods represent actions that you would
      perform on a typical API.

# Add URL Router

Note: Just like with our __APIView__ we need to register our new __ViewSet__ with
      a URL to make it accessible through our API. The way that you register the
      __ViewSets__ with a URL is slightly different from how you register the
      __APIView__ with the URL.

To register __APIView__ with the *hello-view/* URL we used the *path* function in
__profiles_api/urls.py__.

To register __ViewSet__ you have to:
1. Use *Router* (class provided by the Django REST Framework) in order to generate
   the different routes that are available for our __ViewSet__:
    * in __profiles_api/urls.py__ import *include* from *django.urls* and
      *DefaultRouter* from *rest_framework.routers*,
    * to use *DefaultRouter* is you assign the router to a variable,
2. Use *__variable__.register* to register specific __ViewSets__ with our router
   (*"/"* is not needed in __ViewSets'__ URLs).
3. Add the URL to existing *urlpatterns*.

Note: So as you register new routes with our router, it generates a list of URLs
      that are associated for our __ViewSet__. It figures out the URls that are
      required for all of the functions that we add to our __ViewSet__ and then
      it generates this URLs list which we can pass in to using the *path*
      function and the *include* function to our *urlpatterns*.

More informations in __profiles_api/urls.py__.

# Add create, retrieve, update, partial_update and destroy functions

1. Go to __profiles_api/views.py__ and add serializer to *HelloViewSet* class in the same way
   that you added it to the __APIView__.

Note: We can use the same serializer that we created for our __APIView__.

2. Add functions in *HelloViewSet* class.

For more informations head over to __profiles_api/views.py__.

# Test ViewSet

Note: Unlike the API view we do not actually see the put, patch and delete
      methods here on the */hello-viewset* API. That is because __ViewSets__
      expect that you will use this endpoint to retrieve a list of objects in
      the database and you will specify a primary key ID in the URL when making
      changes to a specific object. So if we want to see these additional
      functions that we added, we need to add something to the end of the URL.
      Now in in this case because we are not actually retrieving any real
      objects, it does not matter what you type, but if you just put a number
      here, that would represent a primary key of an object, that you wanted to
      change and hit enter, then it will change the page to the get request.

# Plan our profile API

Now that we know how to make a simple API we can move on to building our
profiles API. Before we get started let's explain the specification of
what we are going to build. Our profile API is going to be able to handle the
following:
  1. creating a profile to handle the registration of new users in the system -
     this will include validating the profile data to ensure that a user provided
     all the required fields,
  2. listing existing profiles so users can find other users in the system - this
     needs to include a way to search for users by email or name,
  3. viewing a specific profile by the profile ID,
  4. updating the profile of the logged in user - users in the system should be
     able to change their name, email address and password for their profile,
  5. provide a way for users to delete their own profile.

So what URLs and methods might our API have? Since our API manages profiles it
makes sense to give it the name *profile*.
  1. So the URL would be __/api/profile/__:
      * the route of the URL will list all profiles -> HTTP GET method is called,
      * create a new profile -> HTTP POST method is called.
  2. If the URL would be __/api/profile/<profile_id>/__    
      * view all the details of a specific profile object -> HTTP GET method is called,
      * update the object -> HTTP PUT or PATCH method is called,
      * remove object completely from the system -> HTTP DELETE method is called.

# Create user profile serializer

1. Import *models* from *profiles_api*.
2. Add a new serializer to the __profiles_api/serializers.py__ file (the
   serializer that we are going to add is model serializer - similar to  
   a regulat serializer except it has a bunch of extra functionality witch makes
   it really easy to work with existing Django database models).
3. Create meta class.

Note: The way that you work with model serializers is you use a meta class to
      configure the serializer to point to a specific model in our project.

For more informations go to __profiles_api/serializers.py__.

# Create profiles ViewSet

Note: Now that we have our *UserProfileSerializer* we can go ahead and create
      a ViewSet to access the serializer through an endpoint.

1. Head over to __profiles_api/views.py__.
2. Import *models* from *profiles_api*.

Note: What we're going to use for our user profile API is something called
      a *Model ViewSet*. The Model ViewSet is very similar to a standard ViewSet
      except it's specifically designed for managing models through our API.
      So it has a lot of the functionality that we need for managing models
      built into it.

3. Create new Model ViewSet - a class called *UserProfileViewSet*.

For more informations head over to __profiles_api/views.py__.

# Register profile Viewset with the URL router - to access it from the browser

1. Open up __profiles_api/urls.py__.
2. If needed import *views* from *profiles_api*.
3. Register ViewSet (more in __profiles_api/urls.py__).

# Create permission class

Note: We want to be able to restrict the users so they can only make changes to
      their own profile in the system. We do that using a Django permissions class.

1. Create a new __profiles_api/permissions.py__ file.
2. Import *permissions* from *rest_framework*.
3. Use this *permission* class as the base for our custom permission class.
4. Define new class method which will be checking if object is requesting
   a safe method or is requsesting method on it self.

Note: Safe method is the method that is not making changes on anything.

For more go to __profiles_api/permissions.py__.

# Add authentication and permissions to ViewSet

1. Go to __profiles_api/views.py__.
2. Import *TokenAuthentication* from *rest_framework.authentication*. The token
   authentication is going to be the type of authentication we use for users to
   authenticate themselves with our API.

Note: Token authentication works by generating a random token string when the
      user logs in and then every request we make to their API that we need to
      authenticate we add this token string to the request and that is effectively
      a password to check that every request made is authenticated correctly.

3. Import *permissions* from *profiles_api*.
4. Head over to *UserProfileViewSet* class and configure this to use the correct
   authentication and permissions classes.

For more go to __profiles_api/views.py__.

# Add search profiles feature

1. Open up __profiles_api/views.py__.
2. Import *filters* from *rest_framework*.
3. Add *filter_backends* and *search_fields* to the *UserProfileViewSet* class.

For more informations head over to the __profiles_api/views.py__ file.

# Create login API ViewSet

Note: Type of authentication we are going to use is called token authentication.
      It works by generating a token which is like a random string when you log
      in and then every request you make to the API that you wish to authenticate
      you include this token in the headers. So every single request that is made
      to the API has a HTTP header. What we do is we add the token to the
      authorization header for the requests that we wish to authenticate (so when
      you make a request like a HTTP GET HTTP PUT PATCH or POST). With that
      request you can provide a header and in our header we are going to add
      a key called authorization and then we are going to pass in this token with
      the request and then when Django REST Framework receives that request it
      can check whether this token exists in the database and retrieve the
      appropriate user for this token.

1. Add an endpoint to API that allows you to generate an authentication token:
   * go to __profiles_api/views.py__ and import *ObtainAuthToken* from
     *rest_framework.authtoken.views* and *api_settings* from *rest_framework.settings*,
   * create *UserLoginApiView* class that inherits from *ObtainAuthToken*.

For more head over to __profiles_api/views.py__.

2. Add a URL to this view to enable it:
   * open up __profiles_api/urls.py__,
   * add a 'login/' path to the *urlpatterns*.

Note: Remember that the *Username* field in the browsable login API is based on
      __profiles_api/models.py/UserProfile's__ *USERNAME_FIELD* variable.

# Set token header using ModHeader extension

1. Open ModHeader extension.
2. In the name field input *Authentication*.
3. Paste in value field *Token ...* <- input created token (to create token go to
   http://127.0.0.1:8000/api/login/ and log in).
4. Check if token authorization works by going to different profiles using only id
   (http://127.0.0.1:8000/api/profile/1/ or http://127.0.0.1:8000/api/profile/3/) -
   you should only be able to make changes on account that has token verified.

# Plan profile feed API

In this section we are going to build an API to handle user profile feed items.
The basic features our API requires:
  * creating new feed items for authenticated users,
  * updating an existing feed item in case the user makes a typo or wants to
    change the content of a feed item they have already posted,
  * deleting an item,
  * viewing other users feed items,

What URLs might our API provide:
1. Route API - */api/feed/* endpoint:
   * list all the feed items in the database,
   * GET (getting a list of all user feed items),
   * POST (creating a new feed item for the authenticated profile).
2. Feed item detail API - */api/feed/<feed_item_id>/* endpoint:
   * GET (getting the details of a specific feed item - this is known as the detail view),
   * PUT and PATCH (updating a feed item),
   * DELETE (deleting the feed item).

# Add new model item

1. Create a new Django model for storing the user profile feed items in the database:
   * open up the __profiles_api/models.py__,
   * import *settings* from *django.conf*,
   * create a new model class called *ProfileFeedItem* and base it from __models.py__ model.

For more head over to the __profiles_api/models.py__ file.

# Create and run model migration

Note: Now that we have added a new model to our app we need to run the migration.

1. Create migration file by typing in terminal *python manage.py makemigrations*.
2. Notice that in __profiles_api/migrations__ appeared new file called *0002_profilefeeditem.py*
   which contains the migration file that will create our model in the database.
   In other words it will create the table in the database with our *ProfileFeedItem* model.
3. Run the migration by running *python manage.py migrate* command in the terminal
   to make the changes in the database.

# Add profile feed model to admin

Note: Now that we have added our profile feed item model we need to register this
      model in the Django admin so we can manage the objects in this table through
      the Django admin interface.

1. Head over to the __profiles_api/admin.py__ file.
2. Register *ProfileFeedItem* to Django admin.

# Create ProfileFeedItem serializer

1. Open up the __profiles_api/serializer.py__.
2. Create new serializer called *ProfileFeedItemSerializer* based on *ModelSerializer*
   from __rest_framework/serializers__.

For more head over to __profiles_api/serializer.py__.

# Create ViewSet for our profile feed item

1. Head over to the __profiles_api/views.py__.
2. Create *UserProfileFeedViewSet* which will inherit from __rest_framework/viewsets/ModelViewSet__.

More informations in __profiles_api/views.py__.

3. Head over to __profiles_api/urls.py__.
4. Register new router.

# Add permissions for feed API

Note: This is to ensure that user can only change his own status and prevent
      others from changing others statuses. It also handles error created while
      unauthorized user wants to change someones status.

1. Open up __profiles_api/permissions.py__.
2. Create *UpdateOwnStatus* class which will be responsible of permissions of
   changing status.
3. Next head over to __profiles_api/views.py__.
4. Import *IsAuthenticatedOrReadOnly* from *rest_framework.permissions*.
5. In *UserProfileFeedViewSet* class add *permission_classes* tuple which will
   contain previously created *UpdateOwnStatus* permission and imported
   *IsAuthenticatedOrReadOnly*.

# Restrict viewing status updates to logged in users only

Note: *IsAuthenticatedOrReadOnly* allows authenticated users to get access to
      the database. If they are not authenticated they are able to read-only.

To restrict viewing status updates to logged in users only just change
*IsAuthenticatedOrReadOnly* to *IsAuthenticated* in the __profiles_api/vies.py__.

# Add SSH key pair to AWS

Note: The reason we do this is so that when we create our server we can connect
      to it using SSH authentication. This is the same method of authentication
      that we use to connect to GitHub.

1. The method is the same but we are going to add the key pair to AWS instead of github:
   * output the content of SSH key pair public file by typing *cat ~/.ssh/id_rsa.__pub__*,
   * copy outputted string,
   * log in to the AWS console,
   * open up *services* option and head over to the *EC2*,

Note: EC2 is where the key pairs can be added for use on our server instances.

   * open up *Key Pair* overlap,
   * click on *Import Key Pair* and set name (best practice is to use authorized
     laptop's name) and then paste the copied public key,
   * hit *import*.

# Create EC2 server instance

1. Open up AWS console and select *services* and *EC2*.

Note: This is where all of our EC2 server instances are in AWS.
      An EC2 server instance is simply just a virtual machine that you can spin
      up and connect to deploy our application.

2. Once you are on the EC2 page click on launch instance to create a new instance.
3. Choose operating system.
4. Select the micro instance.
5. Head over to the *Configure Security Group* and add new rule (*Add Rule*) -
   HTTP on port 80.
6. Click on *Review And Launch* and then *Launch*.
7. Choose your key pair.

# Add deployment script and configs to our project

1. Configure project for deployment:
   * add unzipped __deployed.zip__ file (added to the course) that contains a zip
     of all the scripts and configuration files that we need to deploy our project
     (__profiles-rest-api__),

Note: __deploy/setup.sh__ - script that will be used to setup our server when it
      is first created.

   * update *PROJECT_GIT_URL* variable to our GitHub repository,

Note: __update.sh__ - will be used to update the code on the server whenever we
      make a change. Once the server is set up we need to use the __update.sh__
      script to pull updates or changes from git on to the server.

2. Make changes to __profiles_project/settings.py__ file for it to run better on
   the server:
   * open up __profiles_project/settings.py__ and disable debug mode by deleting
     line with debug and replacing it with *DEBUG = bool(int(os.environ.get('DEBUG', 1)))*,

Note: It is best practice never to run the server in debug mode when it is in
      production (publicly accessible).
      Because we want to run debug mode when we run the server on our vagrant
      server but we want to disable it when we run it on the live server we are
      going to add some logic here to pull in the configuration from an
      environment variable. What this does is it pulls in the value of the
      environment variable called *DEBUG*. We set this environment variable in
      the __deploy/supervisor_profiles_api.conf__ (*DEBUG* to zero). This sets
      the debug environment variable to zero when we run our application. The
      *1* is this syntax because this is the default value if the *DEBUG* does
      not exist. So when we run our application on our Vagrant server we are not
      going to specify *DEBUG = 0* so it is going to default to 1 which is going
      to be converted to *True*. That means when we run our server on our local
      machine it is going to be in debug mode but then when it is running on our
      server, debug mode is going to be disabled.

   * add a *STATIC_ROOT* variable to the bottom of our configuration.

3. Run ***chmod +x deploy/*.sh*** command in terminal opened on our project to
   make sure that these setup scripts are executable. (it runs the *chmod* command
   to set executable to any file that ends in *.sh* in our deployed directory).

Note: So when you send a file to a server the file needs to have the permissions
      to be executable.

# SSH to our server and deploy to server

1. Open up the browser and load up the Amazon console page and head over to
   *services* and *EC2*.
2. Click on *Running Instances* where our instance should be up and running.
3. To SSH to our server:
   * copy *Public DNS (IPv4)*,
   * open up terminal and type *ssh ubuntu@__paste_the_copied_url__*,
   * hit enter and type *yes* when asked.

Note: On this point we are connected to the server.

4. Get the URL for the raw data file for our setup script:
   * open up GitHub repository and head over to the *deploy* directory,
   * choose *setup.sh*,
   * click on *raw* button,
   * copy the URL from the browser.

5. Type *curl -sL __paste_copied_url__ | sudo bash -*.

Note: It runs the *curl* command to download the file and then it passes it into
      *sudo bash*. So this *curl* command is used to retrieve contents from a URL.
      So it is basically a HTTP client in Linux. the *-s* is for running in
      silent mode which means it will not update us with all of the steps when
      it is downloading the file. The *L* is for following redirects. So if there
      is any redirects of this URL then it will automatically follow them to the
      final destination and download the contents. The ***|*** is used to pipe
      the output of one command into another command. So we are going to take the
      output of this curl command and we are going to pass it into *sudo bash*. *bash*
      is what we are going to use to run our script. The *-* is used to signal
      the end of the options provided for bash. So that it knows anything we pass
      in is to be ran on bash and not an option to configure bash.

# Update allowed hosts and deploy changes

1. Open up __profiles_project/settings.py__ and add previously copied *Public DNS (IPv4)*
   and localhost (127.0.0.1).
2. Push changes to GitHub.
3. Run update script on the server to pull the GitHub latest changes.
4. Go to the terminal, connect to the server via SSH and navigate to the location
   on the server where our project files are stored by typing
   *cd /usr/local/apps/profiles-rest-api/* and hitting enter.
5. Run *sudo sh ./deploy/update.sh* to start the update script that will update
   the application based on the latest GitHub changes.

Note: At this point the server is operational and ready to handle user activities.

6. Create a superuser by typing in terminal (make sure that you are on the server
   in the */usr/local/apps/profiles-rest-api*) *sudo env/bin/python manage.py createsuperuser*.
7. Enter email, name and password.
