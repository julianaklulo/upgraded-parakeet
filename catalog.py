categories_list = [
    {'Móveis': ['Sala', 'Cozinha']},
    {'Eletrônicos': ['Celulares', 'Computadores']},
    {'Eletrodomésticos': ['Linha Branca']},
    {'Livros': ['Infanto Juvenil', 'Ficção', 'Poesia']}
]

marketplaces_list = {
    'Mercado Livre': [
        categories_list[0],
        categories_list[1],
        categories_list[2]
    ],
    'B2W': [ 
        categories_list[1],
        categories_list[2],
        categories_list[3]
    ],
    'Magazine Luiza': [
        categories_list[0],
        categories_list[1]
    ]
}

def list_marketplaces():
    marketplaces = [marketplace for marketplace in marketplaces_list.keys()]
    return marketplaces

def list_categories():
    categories = [key for category in categories_list for key in category]
    return categories

def list_subcategories(category_name):
    subcategories = [category[category_name] for category in categories_list if category_name in category.keys()]
    return subcategories[0]