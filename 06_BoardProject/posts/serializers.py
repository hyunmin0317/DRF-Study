from django.db.migrations import serializer
from posts.models import Post
from users.serializers import ProfileSerializer


class PostSerializer(serializer.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes")


class PostCreateSerializer(serializer.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")
