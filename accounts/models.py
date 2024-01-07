from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserAccount(models.Model):
    balance = models.DecimalField(default= 0 , max_digits=12 ,decimal_places=2 )
    user = models.OneToOneField(User, related_name='useraccount', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self) -> str:
        return self.user.username
    
    