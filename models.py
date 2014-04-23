from django.db import models

# Create your models here.
class Deck(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
        
class Case(models.Model):
    decks = models.ManyToManyField(Deck, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title
        
class Card(models.Model):
    cases = models.ManyToManyField(Case, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image_front = models.ImageField(upload_to='djecks/cards/images', blank=True, null=True)
    image_back = models.ImageField(upload_to='djecks/cards/images', blank=True, null=True)
    
    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.image.name