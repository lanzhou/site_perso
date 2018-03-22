from django.conf.urls import url
from cv import views
from django.views.generic import TemplateView, ListView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="liens.html"))
]
