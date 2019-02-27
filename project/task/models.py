from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=256);
    age=models.FloatField();
    #courses=models.ManyToManyField(Course);
    class Meta:
        ordering=('-id',);
        verbose_name="TEACHER";
        verbose_name_plural="All Teachers";
    def __str__(self):
        out="Teacher:"+str(self.name);
        return out;
class Student(models.Model):
       name=models.CharField(max_length=256);
       #courses=models.ManyToManyField(Course);
       class Meta:
        ordering=('-id',);
        verbose_name="STUDENT";
        verbose_name_plural="All Students";
       def __str__(self):
           out="Student:"+str(self.name);
           return out;
class Course(models.Model):
    name=models.CharField(max_length=256);
    teachers=models.ManyToManyField(Teacher);
    students=models.ManyToManyField(Student);
    start=models.DateField();
    end=models.DateField();
    class Meta:
        ordering=('-id',);
        verbose_name="COURSE";
        verbose_name_plural="All Courses";
    def __str__(self):
        out="Course:"+str(self.name);
        return out;