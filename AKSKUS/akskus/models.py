from django.db import models


class UserPost(models.Model):
    name=models.CharField(max_length=30)
    mob_num=models.IntegerField(max_length=10)
    email=models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    def __str__(self):
        return ("name="+self.name + " email="+self.email+" pass="+self.password)





class post(models.Model):
    postname=models.CharField(max_length=50)
    post=models.CharField(max_length=500)

