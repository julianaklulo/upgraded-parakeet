from catalog import list_marketplaces, list_categories, list_subcategories

def marketplaces():
    print("\nMarketplaces:\n")
    marketplaces = list_marketplaces()
    for marketplace in marketplaces:
        print(marketplace)
    menu()

def categories():
    print("\nCategories:\n")
    categories = list_categories()
    for category in categories:
        print(category)
    menu()

def subcategories():
    print("\nSubcategories:\n")
    subcategories = list_subcategories()
    for subcategory in subcategories:
        print(subcategory)
    menu()

def menu():
    option = -1
    while option < 0 or option > 3:
        print("\nChoose an option:")
        print("1 - List all marketplaces")
        print("2 - List marketplace's categories")
        print("3 - List category's subcategories")
        print("--------------------")
        print("0 - Exit")
        option = int(input("\nOption: "))

        if option == 0:
            break
        elif option == 1:
            marketplaces()
        elif option == 2:
            categories()
        elif option == 3:
            subcategories()

if __name__ == '__main__':
    menu()