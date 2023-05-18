
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework_simplejwt.authentication import JWTAuthentication


class GetBooksView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        books = Book.objects.all()
        serializers = BookSerializerOnGet(books, many=True)
        return Response (serializers.data, status=status.HTTP_200_OK)
      
class AddBookView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
   
