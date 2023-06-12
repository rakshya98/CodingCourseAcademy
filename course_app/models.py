from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    duration=models.CharField(max_length=25)
    
    def __str__(self):
        return self.title
    
    
class Instructor(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    qualificatin=models.CharField(max_length=50)
    no_years_experience=models.PositiveSmallIntegerField()


class AddCourse(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    duration=models.CharField(max_length=25)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)