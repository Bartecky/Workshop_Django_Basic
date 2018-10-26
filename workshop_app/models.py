from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=127)
    capacity = models.SmallIntegerField(default=1000)
    pojector_is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)


class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} on {}'.format(self.room, self.date)
