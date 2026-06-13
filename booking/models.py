from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

    def __str__(self):
        return f"<User {self.first_name} {self.last_name}>"

    class Meta:
        db_table = "users"
        ordering = ["first_name", "last_name"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class Reservation(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.IntegerField()
    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="reservations"
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="reservations"
    )

    def __str__(self):
        return f"<Reservation for {self.room} (Place: {self.place}) from {self.start_time} to {self.end_time}>"

    class Meta:
        db_table = "reservations"
        ordering = ["start_time", "end_time"]
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"<Room {self.name}>"

    class Meta:
        db_table = "rooms"
        ordering = ["name"]
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
