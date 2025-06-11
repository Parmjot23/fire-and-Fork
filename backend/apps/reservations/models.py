from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pax = models.PositiveIntegerField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Reservation {self.name}"
