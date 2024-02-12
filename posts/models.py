from django.db.models import *
from account.models import User
from post_category.models import PostCategory

class Post(Model):
    title = CharField(max_length=256,blank=True)
    description = TextField(blank=True)
    created = DateField(auto_now_add=True)
    image = ImageField(upload_to="post_image")
    user = ForeignKey(User, on_delete=CASCADE)
    watch_count = PositiveBigIntegerField(default=0)
    like_count = PositiveBigIntegerField(default=0)
    post_category = ForeignKey(PostCategory, on_delete=CASCADE)
    def __str__(self):
        return self.title
class PostComments(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    post = ForeignKey(Post, on_delete=CASCADE)
    comment = CharField(max_length=512)
