from django.urls import path,include
from .import views

urlpatterns = [
    path('login/',views.login,name = 'login'),
    path('register/',views.register,name = 'register'),
    path('logout/',views.logout,name = 'logout'),
    path('add_friend_req/<id>/',views.addfriendreq,name='addfriendreq'),
    path('delete_friend_req/<id>/',views.deletefriendreq,name='deletefriendreq'),
    path('accept_friend_req/<id>/',views.acceptfriendreq,name='acceptfrientreq')
]
