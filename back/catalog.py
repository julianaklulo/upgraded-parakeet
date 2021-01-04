from data import read_categories, read_marketplaces, write_marketplaces, write_log


def list_marketplaces():
    marketplaces_dict = read_marketplaces()
    marketplaces = [key for key in marketplaces_dict.keys()]
    write_log("List marketplaces")
    return marketplaces


def add_marketplace(marketplace_name, categories):
    marketplace = {marketplace_name: categories}
    write_marketplaces(marketplace)
    write_log(f"Create marketplace {marketplace_name}")


def list_categories():
    categories_dict = read_categories()
    categories = [category for category in categories_dict.keys()]
    write_log("List categories")
    return categories


def list_categories_of_marketplace(marketplace_name):
    marketplaces_dict = read_marketplaces()
    categories = marketplaces_dict[marketplace_name]
    write_log(f"List categories of marketplace {marketplace_name}")
    return categories


def list_subcategories(category_name):
    categories_dict = read_categories()
    subcategories = categories_dict[category_name]
    write_log(f"List subcategories of category {category_name}")
    return subcategories
