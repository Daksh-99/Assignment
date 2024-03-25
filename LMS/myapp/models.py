from django.db import models
from user.models import User

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    teachers = models.ManyToManyField( User, related_name='teachers', blank=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    assignment_file = models.FileField(upload_to='assignments/', blank=True, null=True)
    course = models.ForeignKey(Class, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, blank=True, null=True)
    question_text = models.TextField()
    solution = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text