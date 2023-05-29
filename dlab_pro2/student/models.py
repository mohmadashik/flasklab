from django.db import models

class Student(models.Model):
    rank = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'student'
