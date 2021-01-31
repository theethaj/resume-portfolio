from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()