from django.db import models
from accounts.models import UserAccount
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Books(models.Model):
    user = models.ForeignKey(User ,related_name='book' ,on_delete =models.CASCADE ,null=True,blank = True )
    category = models.ManyToManyField(Category,blank=True,null=True)
    title = models.CharField(max_length =200)
    description = models.TextField()
    image =models.ImageField(upload_to='booklist/media/uploads/')
    borrowing_price =models.DecimalField(default=0, max_digits=10, decimal_places=2,null=True,blank = True)
    borrow_date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


STARCHOICES =[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    Books =models.ForeignKey(Books ,on_delete =models.CASCADE, related_name='reviews' ,null=True,blank = True)
    rating =models.CharField(max_length=10, choices=STARCHOICES,blank=True, null =True)
    body = models.TextField(blank=True, null =True)
    name= models.CharField(max_length=100,blank=True, null =True)
    email = models.EmailField(unique=True,)
    created_time = models.DateTimeField(auto_now_add = True)