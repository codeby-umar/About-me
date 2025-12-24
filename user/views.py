from django.shortcuts import render
from django.views.generic import TemplateView

class Userview(TemplateView):
    template_name = 'user.html'