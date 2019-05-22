from django.contrib import admin

# Register your models here.
from server.models import Occurrence, Post, Comment

admin.site.register(Occurrence)
admin.site.register(Post)
admin.site.register(Comment)
