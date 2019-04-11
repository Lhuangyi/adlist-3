from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.name

class Iso(models.Model):
    name =  models.CharField(max_length=128,unique=True)

class Region(models.Model):
    name =  models.CharField(max_length=128,unique=True)


class States(models.Model):
    name = models.CharField(max_length=128,unique=True)


class Site(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    states = models.ForeignKey(States,on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
