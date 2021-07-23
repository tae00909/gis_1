from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # on_delete=models.CASCADE -> user 객체가 삭제(탈퇴)됬을 때 CASCADE(종속) 같이 모델도 삭제 CASCADE말고 SET_NULL은 계쩡을
    # 탈퇴해도 프로피을 남겨두고 싶을때
    # related_name='profile' 사용시 user.profile이 가능
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')

    # null= True -> 이미지 없어도 만들 수 있게
    image = models.ImageField(upload_to='profile/', null=True)
    # unique 닉넴이 유니크한지
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)
