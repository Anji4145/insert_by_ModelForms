from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=20,primary_key=True)

    def __str__(self) -> str:
        return self.topic_name

class WebPage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete = models.CASCADE)
    sname =  models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10) 

    def __str__(self) -> str:
        return self.sname