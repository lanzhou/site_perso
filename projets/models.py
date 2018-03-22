# -*- coding: utf-8 -*-
from django.db import models

# cur, rst, lyr, elt, ite, sat, tlp, vtm...
class Categorie(models.Model):
    categorie = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.categorie

# es, bf, ig, bs, frt ...
class Moyen(models.Model):
    moyen = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.moyen

# ach, cer, crf, zr, etm, org, fre ...
class Institution(models.Model):
    institution = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s" % self.institution

# FORMAT : Date;Institution;;Somme;Monnais;
# EX     : 21/12/2017;etm;;-24,99;EUR;
class Donnees(models.Model):
    donnees = models.TextField(max_length=1000)
    moyen_donnees = models.ForeignKey('Moyen', on_delete=models.CASCADE)

class DonneesSaisies(models.Model):
    date_utilise = models.DateField(verbose_name ="Date Utilisé")
    somme = models.FloatField()

    institution_donneesSaisies = models.ForeignKey('Institution', on_delete=models.CASCADE)
    moyen_donneesSaisies = models.ForeignKey('Moyen', on_delete=models.CASCADE)
    categorie_donneesSaisies = models.ForeignKey('Categorie', on_delete=models.CASCADE)
