from django.shortcuts import render
from ticket.models import Ticket

def index(request):
    data = Ticket.objects.all()
    return render(request, "index.html", {"data": data})