from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, BooleanField, DateTimeField, TextField


# Create your models here.
class Task(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=255)
    description = TextField(max_length=255)
    complete = BooleanField(default=False)
    create = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.user}'