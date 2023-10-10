from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=20)
    priority = models.IntegerField(default=4)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title