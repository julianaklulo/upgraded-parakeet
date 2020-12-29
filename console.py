from catalog import list_marketplaces, list_categories, list_subcategories

def marketplaces():
    marketplaces = list_marketplaces()
    
    option = -1
    while option < 0 or option > len(marketplaces):
        print("\nMarketplaces:\n")
        for index, marketplace in enumerate(marketplaces):
            print(f"{index + 1} - {marketplace}")
        print("--------------------")
        print("0 - Exit")

        option = int(input("\nChoose a marketplace: "))

        if option == 0:
            exit(1)
        elif option < 0 or option > len(marketplaces):
            print("Invalid option, try again!\n")
        else:
            marketplace = marketplaces[option-1]
            categories(marketplace)
            

def categories(marketplace_name):
    categories = list_categories(marketplace_name)

    option = -1
    while option < 0 or option > len(categories):
        print(f"\nCategories of {marketplace_name}:\n")
        for index, category in enumerate(categories):
            print(f"{index + 1} - {category}")
        print("--------------------")
        print("0 - Go back to Marketplaces")

        option = int(input("\nChoose a category: "))
        
        if option == 0:
            marketplaces()
        elif option < 0 or option > len(categories):
            print("Invalid option, try again!\n")
        else:
            category = categories[option-1]
            subcategories(marketplace_name, category)


def subcategories(marketplace_name, category_name):
    print(f"\nSubcategories of {category_name} in {marketplace_name}:\n")
    subcategories = list_subcategories(category_name)
    for subcategory in subcategories:
        print(subcategory)
    menu()

def menu():
    option = -1
    while option < 0 or option > 1:
        print("\nChoose an option:")
        print("1 - List all marketplaces")
        print("--------------------")
        print("0 - Exit")
        option = int(input("\nOption: "))

        if option == 0:
            exit(1)
        elif option == 1:
            marketplaces()

if __name__ == '__main__':
    menu()