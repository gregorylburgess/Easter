from django.contrib.auth.models import User
from django.db import models

class Relative(models.Model):
    last = models.CharField(max_length=200)
    first = models.CharField(max_length=200)
    middle = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    
class Plot(models.Model):
    cemetary = models.CharField(max_length=200)
    relative = models.ForeignKey(Relative)
    lat = models.CharField(max_length=30)
    long = lat = models.CharField(max_length=30)
    arangement = ("Can","Bundle","Arrangement")
    
class Car(models.Model):
    user = models.ForeignKey(User)
    relatives = {}
    
class Player(models.Model):
    owned_cards = []
    
class PointSet(models.Model):
    player= models.ForeignKey(Player)
    nrg = models.IntegerField()
    env = models.IntegerField()
    dollar = models.IntegerField()
    user = models.IntegerField()

class Card(models.Model):
    name = models.CharField(max_length=200)
    type = ("E_Gen", "Tactical", "Service")
    flavor_text = models.CharField(max_length=300)
    success_val = models.IntegerField()
    success_text = models.CharField(max_length=100)
    fail_text = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    owner = models.ForeignKey(Player)
    def __unicode__(self):
        return self.type + ": " + self.name + self.id 


class GameState(models.Model):
    player1_hand={}
    player2_hand={}
    player1_field={}
    player2_field={}
    player_cards = {}
    neutral_cards= {}
    tactical_deck=[]
    e_gen_deck=[]
    active_player = ("p1","p2")
    phase = ("U","B","R","I","G","R")
    