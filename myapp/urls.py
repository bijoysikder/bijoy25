from django.urls import path
from . import views

urlpatterns =[
    path('',views.deshboard,name='deshboard'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('contact',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('add',views.add,name='add'),
    

]

