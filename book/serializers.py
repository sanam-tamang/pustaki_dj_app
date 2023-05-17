# from rest_framework import serializers
# from drf_writable_nested.serializers import WritableNestedModelSerializer
# from .models import *
# import uuid
# class AuthorSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField()
#     class Meta:
#         model = Author
#         fields = '__all__'
   

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# class BookSerializer(WritableNestedModelSerializer):
#     authors = AuthorSerializer(many=False)
#     class Meta:
#         model = Book
#         fields = '__all__'
#     def create(self,validated_data):
#         authors_data= validated_data.pop('authors')
        
#         try:
#             author = Author.objects.get(id=authors_data['id'])
#         except Author.DoesNotExist:
#             author = Author(id=uuid.uuid1,  name = authors_data['name'])
#             author.save()
           
#         book = Book.objects.create(authors=author, **validated_data)
#         return book
    
        
        


from rest_framework import serializers
from .models import Book, Author, Category

class AuthorSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=155)

class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=155)

class BookSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=155)
    description = serializers.CharField(max_length=500)
    authors = AuthorSerializer(many=False)
    document = serializers.FileField()
    image = serializers.ImageField()
    category = CategorySerializer()
    published_by = serializers.UUIDField()
    published_date = serializers.DateField()

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
     
        book = Book.objects.create(**validated_data)
        author_serializer = AuthorSerializer(data=authors_data, many=False)
        author_serializer.is_valid(raise_exception=True)
        authors = author_serializer.save()
        book.authors.set(authors)
      
        book.save()
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors')
        category_data = validated_data.pop('category')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.document = validated_data.get('document', instance.document)
        instance.image = validated_data.get('image', instance.image)
        instance.published_by_id = validated_data.get('published_by_id', instance.published_by_id)
        instance.published_date = validated_data.get('published_date', instance.published_date)

        author_serializer = AuthorSerializer(instance.authors.all(), data=authors_data, many=True)
        author_serializer.is_valid(raise_exception=True)
        authors = author_serializer.save()
        instance.authors.set(authors)

        category_serializer = CategorySerializer(instance.category, data=category_data)
        category_serializer.is_valid(raise_exception=True)
        category = category_serializer.save()
        instance.category_id = category.id

        instance.save()
        return instance

