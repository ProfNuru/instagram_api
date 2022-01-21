from django.contrib import admin
from .models import (
                    Post, Comment, 
                    Like, Reply)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Reply)