
from django.shortcuts import redirect,get_object_or_404,render
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserChangeForm 
from django.views.generic import ListView ,FormView
from django.contrib.auth import logout,login
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegistrationForm ,UserUpdateForm
from booklist.models  import Books
from accounts.models  import UserAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
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
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

@login_required
def Userlogout(request):
    logout(request)
    return redirect('homepage')


def updateinformation(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.success(request,"Update information successfully!")
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request,'page1/update.html',{'form' : form})
   


 
    
    
class Profile(LoginRequiredMixin,ListView):
    template_name = 'page1/profile.html'
    model = Books
    context_object_name = 'data'
    def get_queryset(self):
        return Books.objects.filter(user =self.request.user)
    

# class Edit(UpdateView):
#     model = User
#     form_class = forms.
#     pk_url_kwarg ='id'
#     success_url = reverse_lazy('show')
#     template_name ='show.html'

# @login_required
# def Return_book(request, id):
#     booklist = get_object_or_404(Books, pk=id)
#     user_account = get_object_or_404(UserAccount, user=request.user)
#     book_price = booklist.borrowing_price #book er price
#     user_account.balance+= book_price
#     # booklist.user =None
#     booklist.delete()
#     user_account.save()
#     booklist.save()
#     return redirect('profile')

        
    
@login_required
def borrow_book(request, id):
    booklist = get_object_or_404(Books, pk=id)
    user_account = get_object_or_404(UserAccount, user=request.user)
    book_price = booklist.borrowing_price
    if user_account.balance >= book_price:
        user_account.balance -= book_price
        user_account.save()
        booklist.user = request.user
        booklist.save()
        messages.success(request, 'Book borrowed successfully!')
        return redirect('profile')
    else:
        messages.error(request, 'You do not have the required amount of money.')
        return redirect('details') 


