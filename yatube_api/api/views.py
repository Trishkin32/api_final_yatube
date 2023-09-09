from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permission import UserPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет получения постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UserPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создание нового поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет получения данных групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (UserPermission,)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет получения комментариев."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (UserPermission,)

    def get_queryset(self):
        """Выбор комметариев по id"""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Создание нового комментария по id."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Вьюсет получения подписчиков."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Получение подписчиков."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Создание подписчика."""
        serializer.save(user=self.request.user)
