from django.db import models

# Create your models here.


class Contact(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True)
    subject = models.TextField()
    
    def __str__(self):
        return self.name

    



class Book(models.Model):
    
     name = models.CharField(max_length=150)
    
     email = models.EmailField(null = True)
    
     service = models. CharField(max_length=150, blank=True)
    
     message = models.TextField()
    
     def __str__(self):
        return self.name


