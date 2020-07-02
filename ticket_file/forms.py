from django import forms
from ticket.models import Ticket

class TicketSubmit(forms.Form):
    TICKET_STATUS = [
        ('NE', 'New'),
        ('IP', 'In Progress'),
        ('DO', 'Done'),
        ('IN', 'Invalid')
    ]

    title = forms.CharField(max_length=50)
    bug = forms.CharField(widget=forms.Textarea)
    ticket_status = forms.CharField(label='ticket status:',
        widget=forms.Select(choices=TICKET_STATUS))