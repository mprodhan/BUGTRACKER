from django.urls import path
from ticket_file import views

urlpatterns = [
    path('ticket_create', views.ticketcreation)
]