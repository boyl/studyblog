# coding=utf-8

from rest_framework import viewsets, permissions

from tool.models import ToolCategory, ToolLink
from oauth.models import Ouser
from blog.models import Article, Timeline, Tag, Category
from .serializers import (UserSerializer, ArticleSerializer, TimelineSerializer,
                          TagSerializer, CategorySerializer, ToolLinkSerializer, ToolCategorySerializer)


class UserListSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ouser.objects.all()
    serializer_class = UserSerializer


class ArticleListSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TagListSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryListSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TimelineListSet(viewsets.ReadOnlyModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class ToolLinkListSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToolLink.objects.all()
    serializer_class = ToolLinkSerializer


class ToolCategoryListSet(viewsets.ReadOnlyModelViewSet):
    queryset = ToolCategory.objects.all()
    serializer_class = ToolCategorySerializer
