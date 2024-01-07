
from django.urls import path
from . import views
urlpatterns = [

   path('details/<int:id>/',views.bookDetails , name='details'),
   path('review/<int:id>/',views.BookDetails.as_view() , name='review'),
]
