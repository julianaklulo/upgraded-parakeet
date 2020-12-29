from data import read_categories, read_marketplaces

categories_dict = read_categories()

marketplaces_dict = read_marketplaces()

def list_marketplaces():
    marketplaces = [key for key in marketplaces_dict.keys()]
    return marketplaces

def list_categories(marketplace_name):
    categories = marketplaces_dict[marketplace_name]
    return categories

def list_subcategories(category_name):
    subcategories = categories_dict[category_name]
    return subcategories