from email.mime import image
from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=20)
    desc=models.CharField(max_length=300)
    published_date=models.DateField()
    category=models.CharField(max_length=40,default="") # data update karne se pehle jaha pe value nahi hai waha pai default ko use karna hai
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self) :
        return self.product_name
    
#   I have to use the code that i get from the Gpt  
    