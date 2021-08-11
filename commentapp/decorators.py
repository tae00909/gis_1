
# 데코리이더 목적이 함수를 받아서 꾸며주는 것
from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated