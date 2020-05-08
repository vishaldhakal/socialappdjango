from django.urls import path,include
from .import views

urlpatterns = [
    path('index/',views.index,name = 'index'),
    path('users/',views.users,name = 'users'),
    path('edit/<id>/',views.edit,name = 'edit'),
    path('delete/<id>/',views.delete,name = 'delete'),
    path('liked/<id>/',views.liked,name = 'likes'),
]
