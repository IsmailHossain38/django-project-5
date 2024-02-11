
from django.urls import path
from . import views
urlpatterns = [
   path('login/', views.Userlogin.as_view(), name ='login'),
   path('register/', views.UserRegistrationView.as_view(), name ='register'),
   path('logout/', views.Userlogout , name ='logout'),
   path('profile/',views.Profile.as_view(), name='profile'),
   path('profile/update',views.updateinformation, name='update'),
   path('borrow_book/<int:id>/', views.borrow_book, name='borrow_book'),
   # path('return_book/<int:id>/', views.Return_book, name='return_book'),
]
