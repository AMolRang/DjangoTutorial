from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    # on_delete 이 객체에 대한 조건을 정의함
    # CASCADE는 이 객체가 사라질 떄 관련 된 fields를 삭제함
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True) # 어디에 upload될 지 경로를 정해준다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

    
