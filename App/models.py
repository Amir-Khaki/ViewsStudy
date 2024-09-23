from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    adderss = models.TextField()

    def get_absolute_url(self):
        return reverse('detail', args=[self.objects.pk])

    def __str__(self) -> str:
        return self.name

