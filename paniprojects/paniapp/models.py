from django.db import models


class place (models.Model):
    name=models.CharField(max_length=280)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class team(models.Model):
    name = models.CharField(max_length=280)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

     # def __str__(self):
     #     return self.name

