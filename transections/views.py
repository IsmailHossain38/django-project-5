from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from .models import Transaction
from .forms import DipositForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.



        
    
class TransactionMixinView(LoginRequiredMixin,CreateView):
    template_name = 'transaction/deposit.html'
    model =Transaction
    success_url = reverse_lazy('profile')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'useraccount': self.request.user.useraccount
        })
        return kwargs
    
class DipositView(TransactionMixinView):
    form_class =DipositForm
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        useraccount = self.request.user.useraccount
        useraccount.balance += amount  
        useraccount.save(update_fields=['balance'])
        messages.success(self.request, f'{amount} deposited successfully!')
        mail_sub ='Deposit Confirmation'
        message =render_to_string('transaction/deposit_email.html',{'user' : self.request.user,'amount':amount, })
        to_email =self.request.user.email
        send_mail= EmailMultiAlternatives(mail_sub,'',to=[to_email])
        send_mail.attach_alternative(message,'text/html')
        send_mail.send()
        
        return super().form_valid(form)
    
    
    
