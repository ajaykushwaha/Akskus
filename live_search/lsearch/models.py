from django.db import models

class key(models.Model):
    k=models.CharField(max_length=50)
    def __str__(self):
        return (self.k)