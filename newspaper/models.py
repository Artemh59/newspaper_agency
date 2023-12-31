from django.contrib.auth.models import AbstractUser
from django.db import models

from newspaper_agency import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    redactor = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="redactor"
    )

    def __str__(self):
        return f"{self.topic}"
