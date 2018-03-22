# -*- coding: utf-8 -*-
from django.shortcuts import render
from projets.models import Institution, Categorie, Moyen, Donnees, DonneesSaisies
from django.views.generic import ListView
from django.db.models import Count, Min, Sum, Avg
from datetime import datetime

class ListeDonnees(ListView):
    model = DonneesSaisies
    context_object_name = "donneesSaisies"
    template_name = "comptes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        donnees = Donnees.objects.values_list('donnees', flat=True)
        listdonnees = ''.join(donnees).split("\r\n")

        moyen_donnees = list(Donnees.objects.values_list('moyen_donnees__moyen', flat=True))
        moy = Moyen.objects.get(moyen=''.join(moyen_donnees))

        for liste in listdonnees :
            data = liste.split(";")
            inst = Institution.objects.get(institution=data[1])
            cate = Categorie.objects.get(categorie=self.traitement_donnees(inst))

            # DonneesSaisies.objects.create(
            #    date_utilise=datetime.strptime(data[0],'%d/%m/%Y'),
            #    institution_donneesSaisies=inst,
            #    somme=float(data[3].replace(",", ".")),
            #    moyen_donneesSaisies=moy,
            #    categorie_donneesSaisies=cate)

        context["donnees"] = listdonnees

        context["sommes"] = DonneesSaisies.objects.aggregate(Sum('somme'))
        context["institutions"] = list(DonneesSaisies.objects.values_list('institution_donneesSaisies__institution', flat=True))
        return context

    def traitement_donnees(self, inst):
        cate = ''
        if inst in ['ach','crf']:
            cate = 'cur'
        elif inst is 'org':
            cate = 'ite'
        elif inst is 'fre':
            cate = 'tlp'
        elif inst is 'zr' or inst is 'etm':
            cate = 'vtm'
        elif inst is 'cer':
            cate = 'lyr'
        return cate
