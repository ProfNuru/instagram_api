from django.urls import path
from .views import (
                    home,
                    RegisterUserView, 
                    PostListView, 
                    PostCreateView,
                    CommentCreateView,
                    LikePostView,
                    ListLikesForPostView,
                    ListCommentView,
                    ReplyCreateView,
                    ListReplyView
                )

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('posts/', PostListView.as_view(), name='list-posts'),
    path('posts/create/', PostCreateView.as_view(), name='create-posts'),
    path('posts/like/', LikePostView.as_view(), name="like-post"),
    path('posts/likes/<int:pk>/', ListLikesForPostView.as_view(), name="like-post"),
    path('posts/comments/create/', CommentCreateView.as_view(), name='create-comments'),
    path('posts/comments/<int:pk>/', ListCommentView.as_view(), name='list-comments'),
    path('posts/comments/reply/', ReplyCreateView.as_view(), name='reply'),
    path('posts/comments/replies/<int:pk>/', ListReplyView.as_view(), name='list-replies'),
]

