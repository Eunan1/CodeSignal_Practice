# Library Catalog
library_catalog = {
    'Moby Dick': 'Herman Melville',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

def is_available(book_name, library_catalog):

    if book_name in library_catalog:
        print("Book available")
    else:
        print("Book unavailable")

book_name1 = '1984'
book_name2 = 'Moby Dick'
ans1 = is_available(book_name1, library_catalog)
ans2 = is_available(book_name2, library_catalog)