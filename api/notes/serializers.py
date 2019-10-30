from rest_framework import serializers

from api.categories.models import Category
from api.notes.models import Note


class NoteListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Note
        fields = (
            'url',
            'uuid',
            'owner',
            'category',
            'title',
            'created',
            'modified',
            'is_favorited',
            'is_published',
        )


class NoteDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Note
        fields = (
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
