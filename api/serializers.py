from attr import fields
from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category', 'status', 'photo', 'body', 'publish', 'created', 'updated']