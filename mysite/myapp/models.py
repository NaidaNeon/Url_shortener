from django.db import models

# Create your models here.
#model for Schools
class School(models.Model):
    name = models.CharField(max_length = 1000)
    amount_of_teachers = models.IntegerField()
    amount_of_students = models.IntegerField()
    is_private = models.BooleanField(default = False)

    #model for Link shortener

class Link(models.Model):
    link = models.CharField(max_length = 1000)
    uuid = models.CharField(max_length = 1000)