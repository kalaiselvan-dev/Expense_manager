from email.policy import default
from pyexpat import model
from django.db import models

from django.contrib.auth.models import User  # Create your models here.


TYPE = (

    ('Positive', 'Positive'),

    ('Negative', 'Negative')

)


# class userdetails(models.Model):
#     username = models.CharField(maxlength=20, blank=False)


class Profile (models.Model):
    username = models.CharField(max_length=100, blank=False)
    income = models.FloatField(default=0)
    expenses = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    balance = models.FloatField(default=0)


class Expense(models.Model):
    username = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
