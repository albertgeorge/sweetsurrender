from django.db import models

class Attribute(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
        
class Item(models.Model):
    image = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    attributes = models.ManyToManyField(Attribute, through='ItemAttribute')
    
    def __unicode__(self):
        return self.name

class ItemAttribute(models.Model):
    item = models.ForeignKey(Item)
    attribute = models.ForeignKey(Attribute)
    attributevalue = models.CharField(max_length=1024)
