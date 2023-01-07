from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes(requests, food):
    servings = int(requests.GET.get('servings', 1))
    ingredients = {}
    for ing, count in DATA[food].items():
        ingredients[ing] = count * servings
    context = {'recipe': ingredients}

    return render(requests, 'calculator/index.html', context=context)

def home(requests):
    context = {'menu': [name for name in DATA.keys()]}
    print(DATA.keys())
    return render(requests, 'calculator/home.html', context)