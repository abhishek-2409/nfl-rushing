from django.db import models

#Creating a player class
class Player(models.Model):
    player = models.CharField(max_length=50)
    team = models.CharField(max_length=5)
    pos = models.CharField(max_length=5)
    att = models.IntegerField()
    att_g = models.DecimalField(max_digits=4, decimal_places=1)
    yds =  models.IntegerField()
    avg = models.DecimalField(max_digits=4, decimal_places=1)
    yds_g = models.DecimalField(max_digits=4, decimal_places=1)
    td = models.IntegerField()
    lng = models.CharField(max_length=4)
    fst = models.IntegerField()
    fst_pc = models.IntegerField()
    rush20p = models.IntegerField()
    rush40p = models.IntegerField()
    fum = models.IntegerField()

    def __str__(self):
        return self.player


