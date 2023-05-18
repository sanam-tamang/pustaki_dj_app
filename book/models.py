from django.db import models
from account.models import User
import uuid
import os

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.published_by.id, uuid.uuid4(), ext)
    return os.path.join('uploads', filename)

class Category(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid1,editable=False)
    name = models.CharField(max_length=155, null=False)

class Book(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4,editable=False)
    title = models.CharField(max_length=155,  null=False)
    description = models.TextField(max_length=500)
    document = models.FileField(upload_to=content_file_name, null=False)
    image = models.ImageField(upload_to=content_file_name, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    published_date = models.DateField(auto_now_add=True, )

