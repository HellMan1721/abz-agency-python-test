from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


def tree(request):
    return render(request, 'tree.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name='users/profile.html'