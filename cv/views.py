#from django.http import HttpResponse
from cv.models import ContratProfessionel, ContratUniversitaire
from django.views.generic import ListView
#from django.shortcuts import render, render_to_response

class ListeContrats(ListView):
    model = ContratProfessionel
    context_object_name = "contratPro"
    template_name = "cv.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contratUniv"]=ContratUniversitaire.objects.all()
        return context
