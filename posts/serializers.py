from rest_framework.serializers import ModelSerializer

from .models import Post, PostComments


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "created",
            "user",
            "watch_count",
            "like_count",
            "post_category"
        )
class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = PostComments
        fields = (
            "id",
            "user",
            "post",
            "comment",
        )

