from django.db import models

# Create your models here.

class Student(models.Model):
    stud_name = models.CharField(max_length=100)
    stud_age = models.IntegerField()
    stud_sch = models.CharField(max_length=100)
    stud_des = models.TextField()
    stud_pass = models.ImageField(upload_to='student/')
    stud_reg = models.IntegerField()

    def __str__(self):
        return self.stud_name

    


