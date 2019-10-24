from django.urls import path

from api.notes import views

urlpatterns = [
    path('', views.NoteList.as_view(), name=views.NoteList.name),
    path('<uuid:pk>/', views.NoteDetail.as_view(), name=views.NoteDetail.name),
]
