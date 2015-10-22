from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):

    name = models.CharField(max_length=100, unique=True)
    logo = models.URLField(unique=True, null=True, blank=True)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Shop(models.Model):

    class Meta:
        unique_together = ('name', 'address')

    name = models.CharField(max_length=100)
    logo = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):

    category = models.ForeignKey('Category')
    source_url = models.URLField()
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField(unique=True)
    summary = models.TextField()
    features = models.TextField(help_text='Add name : value pairs seperated by new line')
    pros = models.TextField(help_text='Add pros seperated by new line')
    cons = models.TextField(help_text='Add cons seperated by new line')
    price = models.FloatField()
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True)
    shops = models.ManyToManyField('Shop', blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    added = models.DateTimeField(auto_now_add=True)
