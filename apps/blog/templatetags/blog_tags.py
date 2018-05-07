from django import template
from django.db.models.aggregates import Count

from ..models import Carousel, Tag, Category, FriendLink

register = template.Library()


# 文章相关标签函数
@register.simple_tag
def get_tag_list():
    '''返回标签列表'''
    return Tag.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)


@register.simple_tag
def get_category_list():
    '''返回分类列表'''
    return Category.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)


@register.inclusion_tag('blog/tags/article_list.html')
def load_article_summary(articles):
    '''返回文章列表模板'''
    return {'articles': articles}


@register.inclusion_tag('blog/tags/pagecut.html', takes_context=True)
def load_pages(context):
    '''分页标签模板，不需要传递参数，直接继承参数'''
    return context


@register.simple_tag
def keywords_to_str(art):
    '''将文章关键词变成字符串'''
    keys = art.keywords.all()
    return ','.join([key.name for key in keys])


# 其他函数
@register.simple_tag
def get_carousel_list():
    '''获取轮播图片列表'''
    return Carousel.objects.all()


@register.simple_tag
def get_friends():
    '''获取活跃的友情链接'''
    return FriendLink.objects.filter(is_show=True, is_active=True)
