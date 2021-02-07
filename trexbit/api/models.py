from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, unique = True)
    age = models.IntegerField()    

    class Meta:
        ordering = ['created']