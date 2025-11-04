from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book

# Create your views here.

# class-based view with added class-based 'protected' 
# view LoginRequiredMixin
class BookListView(LoginRequiredMixin,ListView):
    
    model = Book     # specity the template
    template_name = 'books/main.html'   #specify the template

class BookDetailView(LoginRequiredMixin, DetailView):
    
    model = Book   # specify the model
    template_name = 'books/detail.html'  #specify the template