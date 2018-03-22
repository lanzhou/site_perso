# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.text import Truncator
from cv.models import ContratProfessionel, ContratUniversitaire

# Register your models here.
class ContratProfessionelAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'date_debut', 'date_fin', 'lieu', 'institution', 'type_contrat', 'apercu_contenu')

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ( 'titre', 'lieu', 'institution', 'date_debut', 'date_fin')
        }),
        ('Optionnel', {
            'classes': ['collapse',],
            'fields': ('type_contrat', )
        }),
        # Fieldset 2 : contenu de commentaire
        ('Contenu de contrat', {
           'description': 'Détailler des tâches éffectuées et préciser des outils utilisés :',
           'fields': ('commentaire', )
        }),
    )
    def apercu_contenu(self, contratProfessionel):
        return Truncator(contratProfessionel.commentaire).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


class ContratUniversitaireAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'lieu', 'institution', 'date_debut', 'date_fin', 'specialite', 'parcours', 'apercu_contenu')

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ('titre', 'lieu', 'institution', 'date_debut', 'date_fin')
        }),
        ('Optionnel', {
            'classes': ['collapse',],
            'fields': ('specialite', 'parcours')
        }),
        # Fieldset 2 : contenu de commentaire
        ('Contenu de contrat', {
           'description': 'Détailler des tâches éffectuées et préciser des outils utilisés :',
           'fields': ('commentaire', )
        }),
    )
    def apercu_contenu(self, contratUniversitaire):
        return Truncator(contratUniversitaire.commentaire).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(ContratProfessionel, ContratProfessionelAdmin)
admin.site.register(ContratUniversitaire, ContratUniversitaireAdmin)
