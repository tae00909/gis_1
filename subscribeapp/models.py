from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    class Meta:
        # 지정한 두 쌍이 유일하게 하나만 설정하게 함
        unique_together = ['user', 'project']
