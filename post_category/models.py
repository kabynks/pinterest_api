from django.db.models import *

class PostCategory(Model):
    name = CharField(max_length=256)
    def __str__(self):
        return self.name

