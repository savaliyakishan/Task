from django.db import models


class City(models.Model):
    city = models.CharField(max_length=255,null=False,blank=False,db_column="City")

    def __str__(self):
        return f'{self.id}, {self.city}'

class Component(models.Model):
    id = models.AutoField(primary_key=True,db_column="Id")
    name = models.CharField(max_length=255,null=False,blank=False,db_column="Name")
    phone = models.BigIntegerField(null=False,blank=False,db_column="Phone_Number")
    city = models.ManyToManyField(City)