from django.conf.urls import url

from .views import NotificationView, AddcommentView

urlpatterns = [
    url(r'^add/$', AddcommentView, name='add_comment'),
    url(r'^notification/$', NotificationView, name='notification'),

]
