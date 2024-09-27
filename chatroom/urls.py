from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatrooms, name='chatrooms'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('room/<str:room_name>/send/', views.send_message, name='send_message'),
    path('create/', views.create_chatroom, name='create_chatroom'),
]