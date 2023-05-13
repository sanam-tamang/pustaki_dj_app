from rest_framework import serializers
from account.serializers import UserDetailSerializer

from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=False)
    category = CategorySerializer(many=False)
    published_by =  UserDetailSerializer(many=False, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

