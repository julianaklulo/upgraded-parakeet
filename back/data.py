from datetime import datetime


def write_log(log_line):
    timestamp = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    with open('files/log.txt', 'a') as log_file:
        log_file.write(f"[{timestamp}] {log_line}\n")


def read_categories():
    categories_dict = {}
    with open('files/categories.txt', 'r') as categories_file:
        for line in categories_file:
            line = line.strip()
            category = line.split(';')[0]
            subcategories = [subcategory for subcategory in line.split(';')[1:]]
            categories_dict[category] = subcategories
    return categories_dict


def write_categories(category_dict):
    category = list(category_dict.keys())[0]
    subcategories = ';'.join(category_dict[category])
    with open('files/categories.txt', 'a') as categories_file:
        categories_file.write(category + ';' + subcategories + '\n')


def read_marketplaces():
    marketplaces_dict = {}
    with open('files/marketplaces.txt', 'r') as marketplaces_file:
        for line in marketplaces_file:
            line = line.strip()
            marketplace = line.split(';')[0]
            categories = [category for category in line.split(';')[1:]]
            marketplaces_dict[marketplace] = categories
    return marketplaces_dict


def write_marketplaces(marketplace_dict):
    marketplace = list(marketplace_dict.keys())[0]
    categories = ';'.join(marketplace_dict[marketplace])
    with open('files/marketplaces.txt', 'a') as marketplaces_file:
        marketplaces_file.write(marketplace + ';' + categories + '\n')
