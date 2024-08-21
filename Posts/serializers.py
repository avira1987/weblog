from rest_framework import serializers

from Posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['pk','title', 'text', 'is_enable']