from django.db import models

def djeck_title(obj):
    if obj.title:
        return obj.title
    elif obj.source:
        return obj.source
    else:
        return str(obj.id)

class Deck(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return djeck_title(self)
        
class Case(models.Model):
    SEXES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    
    decks = models.ManyToManyField(Deck, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True, choices=SEXES)
    age = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return djeck_title(self)
        
class Card(models.Model):
    cases = models.ManyToManyField(Case, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_front = models.ImageField(upload_to='djecks/cards/images', blank=True, null=True)
    image_back = models.ImageField(upload_to='djecks/cards/images', blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return djeck_title(self)