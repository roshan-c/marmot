from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField()
    cover = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title