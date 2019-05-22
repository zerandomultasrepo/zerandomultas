import os
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Occurrence(models.Model):
    """
    This class represents a Occurrence.
    """

    def get_upload_path(self, filename):
        return os.path.join(
            "ocorrencia/" + self.email + "/", filename)

    name = models.CharField(max_length=120)
    email = models.EmailField()
    plan = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    traffic_ticket = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    drivers_licence = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    dut_copy = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.email


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


class Comment(models.Model):
    """
    This class represents an user comment.
    """
    name = models.CharField(max_length=120)
    email = models.EmailField()
    comment = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.email
