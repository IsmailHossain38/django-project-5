
from django import forms
from .models import Transaction

from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        self.useraccount = kwargs.pop('useraccount', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.useraccount = self.useraccount
        self.instance.balance_after_transaction = self.useraccount.balance
        return super().save()

    
class DipositForm(TransactionForm):
    def clean_amount(self):
        min_diposit_money =50
        amount = self.cleaned_data.get('amount')
        if amount < min_diposit_money:
            raise forms.ValidationError(f'you need to deposit at-least {min_diposit_money} taka')
        return amount
