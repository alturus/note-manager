from django.urls import path

from api.users import views

urlpatterns = [
    path('', views.UserList.as_view(), name=views.UserList.name),
]
