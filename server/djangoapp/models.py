from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    TYPE_CHOICES = (
        ("SUV", "SUV"),
        ("Sedan", "Sedan"),
        ("Truck", "Truck"),
    )

    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"
