from django.db import models

# Create your models here.
class project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    functionalities = models.TextField()
    languages_used = models.TextField()
    git_link = models.TextField()
    live_link = models.TextField()
    sample1 = models.ImageField(upload_to='port/images', default='')
    sample2 = models.ImageField(upload_to='port/images', default='')
    sample3 = models.ImageField(upload_to='port/images', default='')
    
    def __str__(self):
        return self.name + '(' +str(self.id) +')'
class contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    query = models.TextField()
    
    def __str__(self):
        return self.name