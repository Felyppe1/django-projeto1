from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', {
        'recipes': recipes #[make_recipe() for _ in range(10)]
    }
)

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id  #__ serve para acessar campos da foreign key
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', {
        'recipes': recipes #[make_recipe() for _ in range(10)]
    }
)

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
)