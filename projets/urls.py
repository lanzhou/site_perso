from django.conf.urls import url
from projets import views
from django.views.generic import TemplateView, ListView

urlpatterns = [
    url(r'^$', views.ListeDonnees.as_view())
]
