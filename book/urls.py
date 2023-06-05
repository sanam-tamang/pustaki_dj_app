from django.urls import path
from .views import *

urlpatterns = [
    path('book/list_book/',GetBooksView.as_view()),
    path('book/add/', AddBookView.as_view()),
    path('category/add/',AddCategoryView.as_view()),
    path('category/list_category/',GetCategoryListView.as_view()),

    path('book/category/<uuid:category_id>/', FilterBooksWithCategoryView.as_view(), name='book-by-category'),
    path('book/user/<uuid:published_by_id>/', FilterBooksWithUserView.as_view(), name='book-by-userIdview'),


]
