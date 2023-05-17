from rest_framework import serializers
from .models import *

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
    authors = AuthorSerializer(many=False)
    class Meta:
        model = Book
        fields = '__all__'
    def create(self,validated_data):
        authors_data= validated_data.pop('authors')
        
        try:
            author = Author.objects.get(id=authors_data['id'])
        except Author.DoesNotExist:
            author = Author.objects.create(**authors_data)
           
        book = Book.objects.create(authors=author, **validated_data)
        return book
    
        
        



