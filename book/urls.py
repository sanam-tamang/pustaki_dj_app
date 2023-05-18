from django.urls import path
from .views import *

urlpatterns = [
    path('book/list_book/',GetBooksView.as_view()),
    path('book/add/', AddBookView.as_view()),
    path('category/add/',AddCategoryView.as_view()),
    path('category/list_category/',GetCategoryListView.as_view()),
]
