from django.contrib import admin

# Register your models here.
from djecks.models import Deck, Case, Card

class CaseAdmin(admin.ModelAdmin):
    list_filter = ('decks',)

class CardAdmin(admin.ModelAdmin):
    list_filter = ('cases',)
    
admin.site.register(Deck)
admin.site.register(Case, CaseAdmin)
admin.site.register(Card, CardAdmin)
