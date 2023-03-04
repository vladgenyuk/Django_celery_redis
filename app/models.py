from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, null=False)
    Description = models.CharField(max_length=255, null=False)


class Invoker(models.Model):
    title = models.CharField(default='Invoked', max_length=255)

    def __str__(self):
        return self.title
