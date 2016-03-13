from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    item = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    image = models.ImageField()
    description = models.CharField(max_length=260)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

