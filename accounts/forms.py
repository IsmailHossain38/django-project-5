from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount
from django import forms


# class AccountForm(forms.ModelForm):
#     class Meta:
#       model = UserAccount
#       fields ="__all__"

class UserRegistrationForm(UserCreationForm):
    balance = forms.DecimalField(initial=0 , max_digits=12 ,decimal_places=2 )
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email','balance']
        
    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            balance = self.cleaned_data.get('balance')
            UserAccount.objects.create(
                user = our_user,
                balance  = balance, 
            )
        return our_user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']