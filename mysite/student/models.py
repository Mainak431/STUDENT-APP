from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class department(models.Model):
    D_name = models.CharField(max_length=200,primary_key=True)
    HOD = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def _str_(self):
        return self.D_name


class Post(models.Model):
    EnrollmentID = models.CharField(primary_key=True,null=False,max_length=20)
    Name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Address = models.TextField()
    Department_id = models.ForeignKey(department,on_delete=models.CASCADE)
    Enrollment_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.Enrollment_date = timezone.now()
        self.save()


class marks(models.Model):
    EnrollmentID = models.ForeignKey(Post,on_delete=models.CASCADE)
    tmarks = models.FloatField()
    grade = models.CharField(max_length=20)

    def publish(self):
        self.save()


class faculty(models.Model):
    Name = models.CharField(max_length=200,primary_key=True)
    dname = models.ForeignKey(department,on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def _str_(self):
        return self.Name


class Course(models.Model):
    CourseID = models.CharField(max_length=200,primary_key=True,null=False)
    cname = models.CharField(max_length=200)
    Instructor = models.ForeignKey(faculty,on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.CourseID


class Subwise_marks(models.Model):
    EnrollmentID = models.ForeignKey(Post,on_delete=models.CASCADE)
    C_ID = models.ForeignKey(Course,on_delete=models.CASCADE)
    Marks = models.FloatField()
    class Meta:
        unique_together = (("EnrollmentID", "C_ID"),)
    def publish(self):
        self.save()



