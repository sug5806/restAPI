from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class cls(models.Model):
    cls_type = models.CharField(max_length=10)

    def __str__(self):
        return self.cls_type


class Test(models.Model):
    test_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.test_name


class Student(models.Model):
    name = models.CharField(max_length=20)
    cls_t = models.ForeignKey(cls, on_delete=models.SET_NULL, related_name='type', null=True)
    test = models.ManyToManyField(Test, related_name='test', blank=True)
    date = models.DateField('my_date')

    def __str__(self):
        return self.name + " "

    def get_absolute_url(self):
        return reverse_lazy('student:list')
