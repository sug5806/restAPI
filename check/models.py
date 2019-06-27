from django.db import models
from django.contrib.auth.models import AbstractUser

class cls_type(models.Model):
    cls = models.CharField(max_length=10)

    def __str__(self):
        return self.cls


class name(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class image(models.Model):
    img = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.img


class student(models.Model):
    name = models.ForeignKey(name, on_delete=models.CASCADE, related_name='std_name')
    cls = models.ForeignKey(cls_type, on_delete=models.SET_NULL, null=True, related_name='std_cls')
    img = models.ForeignKey(image, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.CharField(max_length=50)
    attend = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.cls) + " " + str(self.img) + " " + self.attend


class manager(AbstractUser):
    cls = models.CharField(max_length=10)

    def __str__(self):
        return self.username + " " + str(self.cls)