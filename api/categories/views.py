from rest_framework import generics, permissions

from api.categories.models import Category
from api.categories.serializers import CategorySerializer
from api.users.permissions import IsAdminOrReadOnly


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'
    pagination_class = None
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly,
    )


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAdminOrReadOnly,
    )
