from rest_framework.serializers import ModelSerializer
from .models import PostCategory
class PostCategorySerializer(ModelSerializer):
    class Meta:
        model = PostCategory
        fields = (
            "id",
            "name"
        )