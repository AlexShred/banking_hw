
from django.views import generic

from .models import Client, Account, Credit


class Index(generic.ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'clients'


class ClientDetail(generic.DetailView):
    model = Client
