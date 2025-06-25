from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    second_name = models.CharField(max_length=100, blank=False, null=False)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    class_number = models.IntegerField(blank=False, null=False)
    letter = models.CharField(max_length=2, blank=False, null=False)
    email = models.EmailField(max_length=100, blank = True, null= True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name}"

