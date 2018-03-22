# -*- coding: utf-8 -*-
from django.db import models

# Create your models here. CurriculumVitae
class Contrat(models.Model):
    """La structure pour un contrat général"""
    date_debut= models.DateField(verbose_name ="Date début")
    date_fin = models.DateField()

    titre = models.CharField(max_length=50)
    lieu = models.CharField(max_length=20)
    institution = models.CharField(max_length=30)
    commentaire = models.TextField(max_length=300)

    class Meta:
        abstract = True

class ContratProfessionel(Contrat):
    """La structure pour un contrat Professionel"""
    type_contrat = models.CharField(max_length=20, verbose_name ="type de contrat")


class ContratUniversitaire(Contrat):
    """La structure pour un contrat Universitaire"""
    specialite = models.CharField(max_length=50, blank=True, verbose_name ="spécialite")
    parcours = models.CharField(max_length=100, blank=True)
