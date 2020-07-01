from django.shortcuts import render, reverse, HttpResponseRedirect
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
                title = data["title"],
                bug = data["bug"]
            )
        return HttpResponseRedirect(reverse("homepage"))
    form = TicketSubmit()
    return render(request, "ticketsubmit.html", {"form": form})

