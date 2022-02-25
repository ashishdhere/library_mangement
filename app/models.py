from django.db import models

# Create your models here.
class lib(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=30) 
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
    
    class Meta:
        db_table = 'users'
        
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'books'