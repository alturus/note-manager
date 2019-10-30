from django_filters import rest_framework as filters, DateTimeFilter

from api.notes.models import Note


class NoteListFilter(filters.FilterSet):
    from_created = DateTimeFilter(field_name='created', lookup_expr='gte')
    to_created = DateTimeFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Note
        fields = (
            'title',
            'category',
            'from_created',
            'to_created',
            'is_published',
            'is_favorited',
        )
