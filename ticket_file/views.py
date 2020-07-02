from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from ticket.models import Ticket
from custom_user.models import BugUser
from ticket_file.forms import TicketSubmit

def ticketcreation(request):
    if request.method == "POST":
        form = TicketSubmit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket_submit = BugUser.objects.get(id=request.user.id)
            ticket = Ticket.objects.create(
                username = request.user,
                title = data["title"],
                bug = data["bug"],
                ticket_status = data["ticket_status"]
            )
            return HttpResponseRedirect(reverse("submitpage", kwargs={"id": ticket.id}))
    form = TicketSubmit()
    return render(request, "ticketsubmit.html", {"form": form})

# This function will view the ticket submission from ticketcreation fucntion.
def submissionview(request, id):
    buguser = BugUser.objects.filter(id=request.user.id)
    data = Ticket.objects.get(id=id)
    return render(request, "submitview.html", {"buguser": buguser, "data": data})

# This is the profile of the user and the tickets that they filed, worked and resolved.
def userview(request, id):
    username = BugUser.objects.get(id=id)
    data = Ticket.objects.filter(username=username)
    return render(request, "profile.html", {"username": username, "data": data})

# This view edits the tickets.
def ticket_edit(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == "POST":
        form = TicketSubmit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = request.user,
            ticket.title = data["title"],
            ticket.bug = data["bug"],
            ticket.ticket_status = data["ticket_status"]
            ticket.save()
            return HttpResponseRedirect(reverse('submissionview', args=(id,)))
    form = TicketSubmit(initial={
        'username': request.user,
        'title': ticket.title,
        'bug': ticket.bug,
        'ticket_status': ticket.ticket_status
    })
    return render(request, "ticketsubmit.html", {"form": form})