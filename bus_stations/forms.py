from django import forms

from .models import Ticket


class SellTicketForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Ticket
