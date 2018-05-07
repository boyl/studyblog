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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blog.feeds import AllArticleRssFeed


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('oauth.urls', namespace='oauth')),  # oauth,只展现一个用户登录界面
    url(r'^comment/', include('comment.urls', namespace='comment')),  # comment
    url(r'', include('blog.urls', namespace='blog')),
    url(r'account', include('allauth.urls')),
    url(r'^feed/$', AllArticleRssFeed(), name='rss'),  # rss订阅
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加入这个才能显示media文件
