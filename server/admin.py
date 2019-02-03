from django.contrib import admin

# Register your models here.
from server.models import Occurrence, Post

admin.site.register(Occurrence)
admin.site.register(Post)
