from rest_framework import serializers

from api.categories.models import Category
from api.notes.models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Note
        fields = (
            'url',
            'uuid',
            'owner',
            'category',
            'title',
            'body',
            'created',
            'modified',
            'is_favorited',
            'is_published',
        )
