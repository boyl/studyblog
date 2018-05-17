from django.conf.urls import url

from .views import NotificationView, AddcommentView, mark_to_delete, mark_to_read

urlpatterns = [
    url(r'^add/$', AddcommentView, name='add_comment'),
    url(r'^notification/$', NotificationView, name='notification'),
    url(r'^notification/no-read/$', NotificationView, {'is_read': 'false'}, name='notification_no_read'),
    url(r'^notification/mark_to_read/$', mark_to_read, name='mark_to_read'),
    url(r'^notification/mark_to_delete/$', mark_to_delete, name='mark_to_delete'),

]
