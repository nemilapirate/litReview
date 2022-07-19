from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from ticket.forms import TicketForm
from ticket.models import Ticket


class CreateTicket(LoginRequiredMixin, generic.CreateView):
    model = Ticket
    success_url = reverse_lazy('flux')
    template_name = 'ticket/create_ticket.html'
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTicket(LoginRequiredMixin, generic.UpdateView):
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('flux')
    template_name = 'ticket/update_ticket.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteTicket(LoginRequiredMixin, generic.DeleteView):
    model = Ticket
    success_url = reverse_lazy('flux')
    template_name = 'ticket/delete_ticket.html'
