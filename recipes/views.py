from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe

class RecipeCreateView(CreateView):
    model = models.Recipe
    fields = ['title', 'category', 'picture', 'ingredients', 'description']

class RecipeUpdateView(UpdateView):
    model = models.Recipe
    fields = ['title', 'category', 'picture', 'ingredients', 'description']

class RecipeDeleteView(DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

#Curly Bracket is for Browser Tab Name
def about(request):
    return render(request, "recipes/about.html", {'title': 'About Us Page'})

def sweets(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/sweets.html", context)

def pasta(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/pasta.html", context)

def salads(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/salads.html", context)

def rice(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/rice.html", context)

def soups(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/soups.html", context)

def dough(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/dough.html", context)

def meats(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/meats.html", context)

def fish(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/fish.html", context)

def spreads(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/spreads.html", context)

def newrecipe(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/newrecipe.html", context)