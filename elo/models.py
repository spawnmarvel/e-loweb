from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 100, default="")
    raw_text = models.CharField(max_length = 10000)
    sentences = models.BigIntegerField(default=0)
    

    def __str__(self):
        return self.raw_text
