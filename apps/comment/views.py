from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render

from blog.models import Article
from .models import ArticleComment


# Create your views here.


@login_required
@require_POST
def AddcommentView(request):
    if request.is_ajax():
        data = request.POST
        new_user = request.user
        new_content = data.get('content')
        article_id = data.get('article_id')
        rep_id = data.get('rep_id')
        the_article = Article.objects.get(id=article_id)
        if not rep_id:
            new_comment = ArticleComment(author=new_user, content=new_content, belong=the_article, parent=None,
                                         rep_to=None)
        else:
            new_rep_to = ArticleComment.objects.get(id=rep_id)
            new_parent = new_rep_to.parent if new_rep_to.parent else new_rep_to
            new_comment = ArticleComment(author=new_user, content=new_content, belong=the_article, parent=new_parent,
                                         rep_to=new_rep_to)
        new_comment.save()
        new_point = '#com-' + str(new_comment.id)
        return JsonResponse({'msg': '评论提交成功！', 'new_point': new_point})
    return JsonResponse({'msg': '评论失败！'})


@login_required
def NotificationView(request, is_read=None):
    '''展示提示消息列表'''
    now_date = datetime.now()
    return render(request, 'comment/notification.html', context={'is_read': is_read, 'now_date': now_date})
