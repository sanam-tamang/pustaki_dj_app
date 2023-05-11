from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegisterUserView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('detail/',UserDetail.as_view()),
]
