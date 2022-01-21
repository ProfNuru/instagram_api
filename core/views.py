from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import (
                            RegisterUserSerializer, 
                            UserSerializer, 
                            PostSerializer,
                            ListPostSerializer,
                            CommentSerializer,
                            ListCommentSerializer,
                            LikeSerializer,
                            ListPostLikeSerializer,
                            ReplySerializer,
                            ListReplySerializer
                        )
from .models import (
                    Post, Comment, 
                    Like, Reply
                    )


def home(request):
    api_urls = {
        'api/core/register/': 'POST user details to register new user (email,username,password)',
        'api/token/': 'POST login to get JWT access and refresh tokens (login with username,password)',
        'api/token/refresh/': 'POST refresh token to get new JWT access token',
        'api/core/posts/': 'GET all posts',
        'api/core/posts/create/': 'POST to create new post (caption, post<image>)',
        'api/core/posts/like/': 'POST to like post (post<pk>)',
        'api/core/posts/likes/pk/': 'GET likes for post',
        'api/core/posts/comments/create/': 'POST to comment on post (comment, post<pk>)',
        'api/core/posts/comments/pk/': 'GET comments for post',
        'api/core/posts/comments/reply/': 'POST to reply to comment (reply,comment<pk>)',
        'api/core/posts/comments/replies/pk/': 'GET replies for comment',

    }
    return JsonResponse(api_urls)

# Register user
class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
     
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


# List of posts ordered by recent
class PostListView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ListPostSerializer
    queryset = Post.objects.prefetch_related('like_set').all().order_by('-date_posted')


# Create post
class PostCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Like post
class LikePostView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get likes for post
class ListLikesForPostView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ListPostLikeSerializer

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs['pk'])
        return Like.objects.filter(post=post).order_by('-date_liked')


# Create comment on post
class CommentCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Get comments for post
class ListCommentView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ListCommentSerializer

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs['pk'])
        return Comment.objects.filter(post=post).prefetch_related('reply_set').order_by('-date_commented')

# Create reply on comment
class ReplyCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReplySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Get comments for post
class ListReplyView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ListReplySerializer

    def get_queryset(self):
        comment = Comment.objects.get(id=self.kwargs['pk'])
        return Reply.objects.filter(comment=comment).order_by('-date_replied')
