# recipes/urls.py
from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name="recipes-about"),
    path('sweets/', views.sweets, name="recipes-sweets"),
    path('pasta/', views.pasta, name="recipes-pasta"),
    path('salads/', views.salads, name="recipes-salads"),
    path('rice/', views.rice, name="recipes-rice"),
    path('soups/', views.soups, name="recipes-soups"),
    path('dough/', views.dough, name="recipes-dough"),
    path('meats/', views.meats, name="recipes-meats"),
    path('fish/', views.fish, name="recipes-fish"),
    path('spreads/', views.spreads, name="recipes-spreads"),
]