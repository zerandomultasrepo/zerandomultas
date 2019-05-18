from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Occurrence(models.Model):
    """
    This class represents a Occurrence.
    """
    name = models.CharField(max_length=120)
    email = models.EmailField()
    plan = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    traffic_ticket = models.ImageField(null=True, blank=True, upload_to="ocorrencia/teste/")
    drivers_licence = models.ImageField(null=True, blank=True, upload_to="ocorrencia/teste/")
    dut_copy = models.ImageField(null=True, blank=True, upload_to="ocorrencia/teste/")
    paid = models.BooleanField(default=False)


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
