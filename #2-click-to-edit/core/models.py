from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    subject = models.CharField(max_length=80)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
