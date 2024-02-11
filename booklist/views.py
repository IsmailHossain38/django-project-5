
from django.shortcuts import render
from django.views.generic import DetailView 
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models  import Books
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def bookDetails(request,id):
    book =Books.objects.get(pk=id)
    review = book.reviews.all()
    return render(request,'pages/details.html',{'booklist':book ,'review':review})

def find_book(request):
    data = Books.objects.all()
    return render(request, 'pages/find_book.html',{'data':data})

# class BookDetails(DetailView):
#     model = Books
#     pk_url_kwarg = 'id'
#     template_name = 'page1/review.html'
    
#     def post(self,request,*args, **kwargs):
#         Books=self.get_object()
#         review_form = forms.ReviewForm(data=self.request.POST)
#         if review_form.is_valid():
#             new_review = review_form.save(commit=False)
#             new_review.Books = Books
#             new_review.save()
#             messages.success(request,"Your review has been successful")
#         return self.get(request,*args, **kwargs)
    
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         Books = self.object
#         review = Books.reviews.all()
#         review_form = forms.ReviewForm()
#         # context['review'] = review
#         context['review_form'] = review_form
#         # context['booklist'] = Books
#         return context
    
    
class BookDetails(LoginRequiredMixin,DetailView):
    model = Books
    pk_url_kwarg = 'id'
    template_name = 'page1/review.html'
    def post(self,request,*args, **kwargs):
        Books=self.get_object()
        review_form = forms.ReviewForm(data=self.request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.Books = Books
            new_review.save()
            messages.success(request,"Your review has been successful")
            
        return self.get(request,*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Books = self.object
        review = Books.reviews.all()
        review_form = forms.ReviewForm()
        # context['tution'] = tutor
        context['review_form'] = review_form
        # context['review'] = review
        return context