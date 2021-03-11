# this is where URLs for our API are gonna be stored
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()                                                        # we assign the router to a variable
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # then we register specific view sets with our router
                                                                                # this is going to be used for retrieving the URLs in our router if we
                                                                                # ever need to do that using the URL retrieving function provided by Django
router.register('profile', views.UserProfileViewSet)                             # unlike the hello view set that we've registered above we don't
                                                                                # need to specify a base name argument and this is because we have in our
                                                                                # view set a query set object
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),                                             # as we register new routes with our router it generates a list of URLs that
]                                                                               # are associated for our view set...                                                                               # it figures out the URLs that are required
                                                                                # for all of the functions that we add to our view set and then it
                                                                                # generates this URLs list which we can pass in to using the path
                                                                                # function and the include function to our URL patterns
                                                                                # we specify a blank string because we don't want to
                                                                                # put a prefix to this URL, we just want to include all of the
                                                                                # URLs in the base of this URLs file
