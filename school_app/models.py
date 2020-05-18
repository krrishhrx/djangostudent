from django.db import models

# Create your models here.

class Student(models.Model):
    student_rollno = models.IntegerField(max_length=3)
    student_name = models.CharField(max_length=30)
    student_class = models.CharField(max_length=10)
    student_guardian = models.CharField(max_length=30)
    teacher_in_charge = models.CharField(max_length=30)
    class Meta:
        db_table="student"
    
    