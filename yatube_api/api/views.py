from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Post, Group, Follow, User
from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    PostSerializer,
    GroupSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None
    permission_classes = (AuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = None
    permission_classes = (AuthorOrReadOnly, )

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get("id")
        return Comment.objects.filter(post=post_id)
    

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('following',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        following = get_object_or_404(Follow, self.request.user)     
        serializer.save()