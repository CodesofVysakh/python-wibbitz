from django.db import models


class Customer(models.Model):
    image = models.FileField(upload_to="Customer/")


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email