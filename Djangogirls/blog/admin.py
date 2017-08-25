from django.contrib import admin
# Register your models here.
#user requests from->controller acts on request->sent request for data
#to model which spits out view back to user
from .models import Post
admin.site.register(Post)
