
from django.urls import path
from . import views
urlpatterns = [

   path('details/<int:id>/',views.bookDetails , name='details'),
   path('find_book',views.find_book , name='find_book'),
   path('review/<int:id>/',views.BookDetails.as_view() , name='review'),
]
