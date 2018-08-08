from djongo import models


class UserPost(models.Model):
    name = models.CharField(max_length=30)
    mob_num = models.IntegerField()
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return "name=" + self.name + " email=" + self.email + " pass=" + self.password


class Post(models.Model):
    post_name=models.CharField(max_length=50)
    post = models.CharField(max_length=500)

