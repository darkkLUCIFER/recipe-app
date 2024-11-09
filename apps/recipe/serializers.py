from rest_framework import serializers

from apps.recipe.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True}
        }
