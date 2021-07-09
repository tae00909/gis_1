from django.db import models

# Create your models here.

# 장고에서 제공해주는 모델
class NewModel(models.Model):
    # 문자열 필드 (null=False는 무조건 값을 넣어줘야한다는 뜻)
    text = models.CharField(max_length=255, null=False)
