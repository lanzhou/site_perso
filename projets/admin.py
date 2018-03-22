# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.text import Truncator
from projets.models import Institution, Categorie, Moyen, Donnees, DonneesSaisies

class CategorieAdmin(admin.ModelAdmin):
    list_display   = ('categorie', )

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ( 'categorie', )
        }),
    )



class MoyenAdmin(admin.ModelAdmin):
    list_display   = ('moyen', )

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ( 'moyen', )
        }),
    )

class InstitutionAdmin(admin.ModelAdmin):
    list_display   = ('institution', )

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ( 'institution', )
        }),
    )

class DonneesAdmin(admin.ModelAdmin):
    list_display   = ('moyen_donnees', 'donnees' )

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ( 'donnees', 'moyen_donnees' )
        }),
    )

class DonneesSaisiesAdmin(admin.ModelAdmin):
    list_display   = ('date_utilise', 'institution_donneesSaisies', 'somme', 'moyen_donneesSaisies', 'categorie_donneesSaisies' )

    fieldsets = (
        # Fieldset 1 : meta-info (date_debut, date_fin…)
       ('Général', {
            'fields': ( 'date_utilise', 'institution_donneesSaisies', 'somme', 'moyen_donneesSaisies', 'categorie_donneesSaisies' )
        }),
    )

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Moyen, MoyenAdmin)
admin.site.register(Donnees, DonneesAdmin)
admin.site.register(DonneesSaisies, DonneesSaisiesAdmin)
