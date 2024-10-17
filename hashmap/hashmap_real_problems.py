# Real World Problem: Example 1 - Library Catalog
def library_catalog(request):

    library_catalog = {}

    book_id = '123'
    book_details = {'Book':'Best Programmer Ever', 'Author': 'Eunan Gavin', 'Release Year': 2024}

    library_catalog[book_id] = book_details

    if book_id in library_catalog:
        print(library_catalog[book_id])

    if request == 'Delete':
        del library_catalog[book_id]



# Real World Problem: Example 2 - Counting Election Vots
def count_votes():
    votes_list = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
    votes_count = {}

    for name in votes_list:

        if name in votes_list:
            votes_count[name] += 1
        else:
            votes_count[name] = 1

    print(votes_count)


# Real World Problem: Example 3 - Tracking Store Inventories
def track_inventory():
    # TODO: Initializing an inventory
    inventory = {'Apples': 50, 'Banannas': 30, 'Oranges': 60}

    # TODO: Adding a new product to inventory and setting its quantity
    inventory['Pears'] = 20

    # TODO: Updating number of apples in inventory
    inventory['Apples'] += 20

    # TODO: Check if a product is in stock or not
    prod = 'Mangoes'
    if prod in inventory:
        print('Success')
    else:
        print('Fail')

