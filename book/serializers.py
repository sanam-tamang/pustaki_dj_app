from rest_framework import serializers
from .models import *
from account.serializers import UserDetailSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

#this is for post
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
## this is for get 
class BookSerializerOnGet(serializers.ModelSerializer):
    Category = CategorySerializer(many=False, read_only=True)
    published_by = UserDetailSerializer(many=False, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'
        

