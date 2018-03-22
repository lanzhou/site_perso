from django.test import TestCase
from cv.models import ContratProfessionel, ContratUniversitaire
# Create your tests here.

class ContratProfessionelCase(TestCase):
    def setUp(self):
        ContratProfessionel.objects.create(
            date_debut="", date_fin="",
            titre="", lieu="",
            institution="", commentaire="",
            type_contrat="")

        ContratUniversitaire.objects.create(
            date_debut="", date_fin="",
            titre="", lieu="",
            institution="", commentaire="",
            specialite="", parcours="")

     def test_contratpro(self):
         cp = ContratProfessionel.objects.get(titre="")
         self.assertEqual(,)
