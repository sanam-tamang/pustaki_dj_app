from rest_framework import serializers
from account.serializers import UserDetailSerializer

from .models import *
import uuid
class AuthorSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Author
        fields = '__all__'
   

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()
    category = CategorySerializer()
    published_by =  UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Book
        fields = '__all__'
    def create(self,validated_data):
        authors_data= validated_data.pop('authors')
        category_data= validated_data.pop('category')
        user_data= validated_data.pop('published_by')
       
        try:
            category = Category.objects.get(id=category_data['id'])
        except Category.DoesNotExist:
            raise ValueError("Category Doesnot exists")
        
        try:
            user = User.objects.get(id=user_data['id'])
        except User.DoesNotExist:
            raise ValueError("User Doesnot exists")
        
        try:
            author = Author.objects.get(id=authors_data['id'])
        except Author.DoesNotExist:
            author = Author(id=uuid.uuid1, name= authors_data['name'] , created_by = user)
            author.save()
          
        
        book = Book.objects.create(authors=author, category=category, published_by=user, **validated_data)
        return book
        



