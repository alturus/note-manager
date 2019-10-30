from rest_framework import generics, permissions

from api.notes.models import Note
from api.notes.serializers import NoteListSerializer, NoteDetailSerializer
from api.users.permissions import IsAdminOrOwner


class NoteList(generics.ListCreateAPIView):
    serializer_classes = {
        'list': NoteListSerializer,
        'create': NoteDetailSerializer,
    }
    name = 'note-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        action = 'create' if self.request.method == 'POST' else 'list'
        return self.serializer_classes[action]

    def get_queryset(self):
        queryset = Note.objects.all()

        if not self.request.user.is_admin:
            queryset = queryset.filter(owner=self.request.user.pk)

        return queryset

    filter_fields = (
        'title',
        'category',
        'created',
        'is_published',
        'is_favorited',
    )
    search_fields = ('title', )
    ordering_fields = (
        'title',
        'category',
        'created',
        'modified',
        'is_favorited',
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer
    name = 'note-detail'
    permission_classes = (
        permissions.IsAuthenticated,
        IsAdminOrOwner,
    )
