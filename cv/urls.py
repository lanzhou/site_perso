from django.conf.urls import url
from cv import views
from django.views.generic import TemplateView, ListView

urlpatterns = [
    url(r'^$', views.ListeContrats.as_view())
]
