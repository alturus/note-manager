from rest_framework import serializers

from api.categories.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
# class CategorySerializer(serializers.ModelSerializer):
    # notes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='note-detail',
    # )

    class Meta:
        model = Category
        fields = (
            'url',
            'uuid',
            'name',
            'description',
            # 'notes',
        )
