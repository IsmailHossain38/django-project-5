
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.views import LoginView 
from django.views.generic import ListView ,FormView
from django.contrib.auth import logout,login
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegistrationForm
from booklist.models  import Books
from accounts.models  import UserAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class Userlogin(LoginView):
    template_name = 'page1/register.html'
    def form_valid(self, form):
        messages.success(self.request,'logged in successfully!')
        return super().form_valid(form)
    def form_invalid(self, form): 
        messages.success(self.request,'logged information incorrect!')
        return super().form_invalid(form)
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    

class UserRegistrationView(FormView):
    template_name = 'page1/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

@login_required
def Userlogout(request):
    logout(request)
    return redirect('homepage')




 
    
    
class Profile(LoginRequiredMixin,ListView):
    template_name = 'page1/profile.html'
    model = Books
    context_object_name = 'data'
    def get_queryset(self):
        return Books.objects.filter(user =self.request.user)
    

@login_required
def Return_book(request, id):
    booklist = get_object_or_404(Books, pk=id)
    user_account = get_object_or_404(UserAccount, user=request.user)
    book_price = booklist.borrowing_price #book er price
    user_account.balance+= book_price
    booklist.user =None
    booklist.delete()
    user_account.save()
    booklist.save()
    return redirect('profile')

        
           
    
    
@login_required
def borrow_book(request, id):
    booklist = get_object_or_404(Books, pk=id)
    user_account = get_object_or_404(UserAccount, user=request.user)
    book_price = booklist.borrowing_price
    if user_account.balance > book_price:
        user_account.balance -= book_price
        user_account.save()
        booklist.user = request.user
        booklist.save()
        messages.success(request, 'Book borrowed successfully!')
        return redirect('profile')
    else:
        messages.error(request, 'You do not have the required amount of money.')
        return redirect('profile') 


