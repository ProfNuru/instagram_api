from xml.etree.ElementTree import Comment
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import (
                    Post, Comment, 
                    Like, Reply
                    )

# Register User Serializer
class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    class Meta:
        model = User
        fields = (
                'email',
                'username',
                'password',
            )
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                            email=validated_data['email'],
                            password = validated_data['password'])
        return user
        

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# Post Serializer for creating posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'caption', 'post'
        )

# Post Serializer for ListAPIView
class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# Comment Serializer for creating comments
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'comment',
            'post'
        )

# Comment Serializer for ListAPIView
class ListCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


# Like Serializer for creating likes on posts
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post',)


# Like serializer for listing likes of Post in ListAPIView
class ListPostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


# Reply Serializer for creating replies on comment
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = (
            'reply',
            'comment'
        )


# Reply Serializer for listing replies for comment
class ListReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"

