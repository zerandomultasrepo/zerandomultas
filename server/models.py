from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Occurrence(models.Model):
    """
    This class represents a Occurrence.
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    plan = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    traffic_ticket = models.TextField()
    drivers_licence = models.TextField()
    dut_copy = models.TextField()
    value = models.FloatField(default=0.0)

class Post(models.Model):
    """
    This class represents a post from admin's blog.
    """

    title = models.CharField(max_length=255)
    summary = RichTextField(default="Post Summary")
    content = RichTextUploadingField(default="Post Content")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
