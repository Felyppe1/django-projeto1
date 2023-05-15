from django.shortcuts import render, get_object_or_404, get_list_or_404
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
    """ recipes = Recipe.objects.filter(
        category__id=category_id, #__ serve para acessar campos da foreign key
        is_published=True  
    ).order_by('-id')

    if not recipes:
        raise Http404('Not found') """
    
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True  
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', {
        'recipes': recipes, #[make_recipe() for _ in range(10)]
        'title': f'{recipes[0].category.name} - Category | '
    }
)

def recipe(request, id):
    """ recipe = Recipe.objects.filter(
        pk=id,
        is_published=True
    ).order_by('-id').first() """

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': recipe,
        'is_detail_page': True,
    }
)