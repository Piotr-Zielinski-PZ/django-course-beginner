from django.contrib import admin                                                # in this file we can add new admins
from profiles_api import models                                                 # first we have to import models from profiles_apiuserprofile
                                                                                # then we register admin...
admin.site.register(models.UserProfile)                                         # this tells django to regirter our UserProfile model with the admin so it's accesible through the admin interface
                                                                                # long story short it registers our admin profile 

# Register your models here.
