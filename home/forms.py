from django.forms import ModelForm, TextInput, Textarea
from contact.models import SendNumber, Aloqa
from django.utils.translation import gettext_lazy as _


class AloqaForm(ModelForm):
    class Meta:
        model = Aloqa
        fields = ['name', 'email', 'subject', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Mavzu'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Sizning xabaringiz'}),
        }


class SendNumberForm(ModelForm):
    class Meta:
        model = SendNumber
        fields = ['phone']
        widgets = {
            'phone': TextInput(attrs={'class': 'input-newsletter', 'placeholder': 'Enter phone number...'}),
        }
