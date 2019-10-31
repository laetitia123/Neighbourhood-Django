from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.


admin.site.register(Neighbour)
admin.site.register(Business)
admin.site.register(Contact)
admin.site.register(Post)

