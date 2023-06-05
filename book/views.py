
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from pustaki.pagination_class import CustomPageNumberPagination
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

class GetBooksView(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializerOnGet


class AddBookView(APIView):
    parser_classes = [MultiPartParser,FormParser]

    def post(self, request):
        request.data['document'].name = content_file_name(request.data['document'], request.data['document'].name)
        request.data['image'].name = content_file_name(request.data['image'], request.data['image'].name)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class  AddCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  GetCategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        categoryList = Category.objects.all()
        serializers = CategorySerializer(categoryList, many=True)
        return Response (serializers.data, status=status.HTTP_200_OK)
   


#this will help to filter the data base on category_id
class  GetCategoryWithBookView(ListAPIView):
    # permission_classes = [IsAuthenticated]
     pagination_class = CustomPageNumberPagination
     serializer_class = BookSerializerOnGet

     def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Book.objects.filter(category_id=category_id)
        return queryset
 
   
