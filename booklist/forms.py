from django import forms 
from .models import Books , Review
class BookForm(forms.ModelForm):
    class  Meta:
        model = Books
        fields =['title','description','image','borrowing_price']
        

class ReviewForm (forms.ModelForm):
    class Meta:
        model = Review
        fields=['rating','body','name','email']   

    