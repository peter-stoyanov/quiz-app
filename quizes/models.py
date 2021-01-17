import uuid

from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(blank=False, max_length=40)
    uuid = models.CharField(max_length=40, null=True, blank=True, unique=True)

    def __init__(self, *args, **kwargs):
        super(Quiz, self).__init__(*args, **kwargs)
        if self.uuid is None:
            self.uuid = str(uuid.uuid4())


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
