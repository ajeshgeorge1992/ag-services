from django.db import models

# Create your models here.
class Winner(models.Model):
    date = models.DateTimeField(null=False)
    winner = models.CharField(max_length=255)
    draw_tiem =models.CharField(max_length=10)
    w1 = models.IntegerField()
    w2 = models.IntegerField()
    w3 = models.IntegerField()
    w4 = models.IntegerField()
    w5 = models.IntegerField()
    w6 = models.IntegerField()
    w7 = models.IntegerField()
    w8 = models.IntegerField()
    w9 = models.IntegerField()
    w10 = models.IntegerField()
    w11 = models.IntegerField()
    w12 = models.IntegerField()
    w13 = models.IntegerField()
    w14 = models.IntegerField()
    w15 = models.IntegerField()
    w16 = models.IntegerField()
    w17 = models.IntegerField()
    w18 = models.IntegerField()
    w19 = models.IntegerField()
    w20 = models.IntegerField()

    