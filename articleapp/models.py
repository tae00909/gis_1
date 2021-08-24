from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    # 1대 다로 연결이 가능한 키
    # models.SET_NULL 사용자가 삭제되더라도 누군가 작성한 페이지가 남음
    # target_user.article
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    # auto_now_add=True -> db에서 정보가 생성될때 시간을 찍어줌
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)