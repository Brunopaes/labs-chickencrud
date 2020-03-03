from django.utils import timezone
from django.db import models


class Sex(models.Model):
    sex = models.CharField(max_length=10)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sex


class People(models.Model):
    name = models.CharField(max_length=100)
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    name = models.ForeignKey(People, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
