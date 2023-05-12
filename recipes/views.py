from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.http import Http404

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', {
        'recipes': recipes #[make_recipe() for _ in range(10)]
    }
)

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, #__ serve para acessar campos da foreign key
        is_published=True  
    ).order_by('-id')

    if not recipes:
        raise Http404('Not found')

    return render(request, 'recipes/pages/category.html', {
        'recipes': recipes, #[make_recipe() for _ in range(10)]
        'title': f'{recipes.first().category.name} - Category | '
    }
)

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
)