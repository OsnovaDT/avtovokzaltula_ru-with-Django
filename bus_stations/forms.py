from django import forms

from .models import SellTicket


class SellTicketForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = SellTicket
