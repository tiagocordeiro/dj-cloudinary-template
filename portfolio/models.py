from django.db import models
from django.utils import timezone

class Trabalho(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name