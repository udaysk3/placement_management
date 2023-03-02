from django.db import models

# Create your models here.
User_Choices = (
    ('Recruiter','Recruiter'),
    ('University','University'),
)
class User(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    password = models.CharField(max_length=1200)
    Role = models.CharField(max_length=20,choices=User_Choices,default='College')
    
    def __str__(self):
        return self.name
