from django.shortcuts import render
from booklist.models import Books
from categories.models import Category
def home(request ,Category_slug =None):
    data = Books.objects.all()
    form = Category.objects.all()
    # review = data.reviews.all()
    if Category_slug is not None:
        category = Category.objects.get(slug = Category_slug)
        data = Books.objects.filter(category=category)
    return render(request, 'home.html',{'data':data , 'category':form })




