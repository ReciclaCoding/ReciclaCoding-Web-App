from django.db import models
from django.utils import timezone


class Note(models.Model):
    note_title = models.CharField(max_length=50)
    note_content = models.TextField(max_length=300)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.note_title


class Register1(models.Model):
    register_recycle = models.CharField(max_length=50)
    register_place = models.CharField(max_length=200)

    def __str__(self):
        return self.register_recycle


class Register2(models.Model):
    register_worker_name = models.CharField(max_length=50)
    register_worker_place = models.CharField(max_length=200)
    register_worker_age = models.PositiveSmallIntegerField(default=20)
    recycle = models.ForeignKey(Register1, on_delete=models.CASCADE)

    def __str__(self):
        return self.register_worker_name
