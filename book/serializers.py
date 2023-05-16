from rest_framework import serializers
from account.serializers import UserDetailSerializer

from .models import *
import uuid
class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    class Meta:
        model = Author
        fields = '__all__'
   

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()
    # category = CategorySerializer()
    # published_by =  UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Book
        fields = '__all__'
    def create(self,validated_data):
        authors_data= validated_data.pop('authors')
       
       
        
       
        
        try:
            author = Author.objects.get(id=authors_data['id'])
        except Author.DoesNotExist:
            author = Author(id=uuid.uuid1, name= authors_data['name'])
            author.save()
          
        
        book = Book.objects.create(authors=author, **validated_data)
        return book
        



