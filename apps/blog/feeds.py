# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.syndication.views import Feed

from .models import Article


class AllArticleRssFeed(Feed):
    title = settings.SITE_END_TITLE  # 显示在聚会阅读器上的标题

    link = "/"  # 跳转网址，为主页

    description = settings.SITE_DESCRIPTION  # 描述内容

    def items(self):  # 需要显示的内容条目，这个可以自己挑选一些热门或者最新的博客
        return Article.objects.all()[:100]

    def item_title(self, item):  # 显示的内容的标题,这个才是最主要的东西
        return "【{}】{}".format(item.category, item.title)

    def item_description(self, item):  # 显示的内容的描述
        return item.body_to_markdown()
