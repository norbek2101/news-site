from django.shortcuts import render
from django.views.generic import TemplateView


class BoshSahifaView(TemplateView):
    template_name = "bosh-sahifa.html"
