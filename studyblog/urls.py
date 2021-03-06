"""studyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from rest_framework.routers import DefaultRouter

from blog import api_views
from blog.feeds import AllArticleRssFeed
from blog.sitemaps import ArticleSitemap, CategorySitemap, TagSitemap


router = DefaultRouter()
router.register(r'users', api_views.UserListSet)
router.register(r'articles', api_views.ArticleListSet)
router.register(r'tags', api_views.TagListSet)
router.register(r'categorys', api_views.CategoryListSet)
router.register(r'timelines', api_views.TimelineListSet)
router.register(r'tools', api_views.ToolLinkListSet)
# router.register(r'tools/categories', api_views.ToolCategoryListSet)


# 网站地图
sitemaps = {
    'articles': ArticleSitemap,
    'tags': TagSitemap,
    'categories': CategorySitemap
}

urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^accounts/', include('allauth.urls')),  # allauth
      url(r'^accounts/', include('oauth.urls', namespace='oauth')),  # oauth,只展现一个用户登录界面
      url(r'^comment/', include('comment.urls', namespace='comment')),  # comment
      url(r'^tool/', include('tool.urls', namespace='tool')),  # tool
      url(r'', include('blog.urls', namespace='blog')),
      url(r'^feed/$', AllArticleRssFeed(), name='rss'),  # rss订阅
      url(r'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  # 网站地图
      url(r'^api/', include(router.urls, namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加入这个才能显示media文件
