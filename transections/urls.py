
from django.urls import path
from . import views
urlpatterns = [
   path('deposit/', views.DipositView.as_view() , name ='deposit'),
   
   
]