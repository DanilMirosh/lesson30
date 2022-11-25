from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO опишите модель кастомного пользователя ниже
class CustomUser(AbstractUser):
    TEACHER = "teacher"
    STUDENT = "student"
    ROLE = [(TEACHER, TEACHER), (STUDENT, STUDENT)]

    birth_date = models.DateField()
    role = models.CharField(max_length=7, choices=ROLE)

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()
