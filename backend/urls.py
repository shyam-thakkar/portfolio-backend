from django.contrib import admin
from django.urls import path
from chat.views import chat_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", chat_api),
]
