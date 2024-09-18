from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    adderss = models.TextField()

    def __str__(self) -> str:
        return self.name

