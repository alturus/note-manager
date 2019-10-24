from django.urls import path

from api.categories import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('<uuid:pk>/', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
]
