from django.conf.urls import url

from .views import (IndexView, MySearchView, TimelineView, DetailView,
                    CategoryView, AboutView, TagView, ArchiveView
                    )

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 主页
    url(r'^hot/$', IndexView.as_view(), {'sort': 'v'}, name='index_hot'),  # 主页，按照浏览量排序
    url(r'^search/$', MySearchView.as_view(), name='search_view'),  # 全文搜索
    url(r'^timeline/$', TimelineView.as_view(), name='timeline'),  # timeline页面
    url(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),  # 文章内容页
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='category'),
    url(r'^category/(?P<slug>[\w-]+)/hot/$', CategoryView.as_view(), {'sort': 'v'}, name='category_hot'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagView.as_view(), name='tag'),
    url(r'^tag/(?P<slug>[\w-]+)/hot/$', TagView.as_view(), {'sort': 'v'}, name='tag_hot'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),  # 归档页面
    url(r'^about/$', AboutView, name='about'),  # About页面

]
