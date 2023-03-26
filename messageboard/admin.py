from django.contrib import admin
from messageboard.models import UserModel, Postmodel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(Postmodel)
