from django.db import models
from accounts.models import UserAccount
from django.contrib.auth.models import User
# Create your models here.
class Transaction(models.Model):
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    balance_after_transection = models.DecimalField( default =0,max_digits=12, decimal_places=2)
    useraccount =models.ForeignKey(UserAccount, on_delete=models.CASCADE,blank =  True , null = True)
    date = models.DateTimeField( auto_now_add=True)
    
    
    
