from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField(max_length=20)
    time = models.TimeField(max_length=20)
    people = models.IntegerField(default=0)
    message = models.TextField()


class Pay(models.Model):
    phone = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)


