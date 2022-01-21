from django.contrib.auth.models import User
from django.db import models
from PIL import Image



class Post(models.Model):
    caption = models.TextField()
    post = models.ImageField(default='default.PNG',upload_to='post_pics')
    date_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User, through='Like', related_name='liked_posts')

    def __str__(self):
        return self.caption


class Comment(models.Model):
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['post','user']]

    def __str__(self):
        return f'{self.user.username} likes {self.post.caption}'


class Reply(models.Model):
    reply = models.TextField()
    date_replied = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply

