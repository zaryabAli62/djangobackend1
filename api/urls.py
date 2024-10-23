
from django.urls import path
from .views import ProjectViewSet, register, login
from .utils import token_required  # Import the token middleware function

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('projects/',token_required( ProjectViewSet.as_view({'get': 'list', 'post': 'create'}))),
    path('projects/<int:pk>/', token_required(ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))),
]
