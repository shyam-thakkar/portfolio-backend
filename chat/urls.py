from django.urls import path
from chat.views import chat_api

urlpatterns = [
    path("chat/", chat_api),
]
