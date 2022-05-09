from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.create_to_do, name='createTodo'),
    path('doneTodo/', views.done_to_do, name='doneTodo')
]
