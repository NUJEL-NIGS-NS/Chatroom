from django.db import models

# Create your models here.
class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timetamp = models.DateField(auto_now=True)
    name = models.CharField(max_length=255)
    group = models.ForeignKey('Group',on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    