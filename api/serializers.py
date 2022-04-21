from blog.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category', 'status', 'photo', 'body', 'publish', 'created', 'updated']