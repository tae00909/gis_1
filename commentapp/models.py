from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    # 게시글 작성자와 연결(누구와 연결? -> User)
    # SET_NULL: 그사람이 탈퇴해도 남아있음
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    # 게시글과 연결
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)

    # 내용 입력 (null=false는 내용이 있어야 입력가능)
    content = models.TextField(null=False)

    # 만든 날짜
    created_at = models.DateTimeField(auto_now_add=True)
