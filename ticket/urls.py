from django.urls import path
from ticket import views

urlpatterns = [
    path('home', views.index, name='homepage')
]

