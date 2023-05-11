from django.db import models
from account.models import User
import uuid

class Author(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid1,editable=False)
    name = models.CharField(max_length=155)
class Category(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid1,editable=False)
    name = models.CharField(max_length=155, null=False)

class Book(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4,editable=False)
    title = models.CharField(max_length=155,  null=False)
    description = models.TextField(max_length=5000)
    authors = models.ManyToManyField(Author, )
    document = models.FileField(upload_to='files/', null=False)
    image = models.ImageField(upload_to='images/', null=False)
    category = models.ManyToManyField(Category, )
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    published_date = models.DateField(auto_now_add=True, )

