# Create a catalog for the library using dictionaries

library_catalog = {'book 1': 'A Tale of Two Cities',
                   'book 2': 'To Kill a Mockingbird',
                   'book 3': '1984'
                   }


# dictionary_number = {key: value}

# Values can be mutable or immutable 
# keys must be immutable = Strings, numbers, tuples
# Values are stored and received in the same order they are found

# Hashmap Operations: Create, Read, Update, Deletes

# Addition, Updating, Locating: O(1) Time complexity 


# We can retrieve a book's title using its key in a straightforward way

# 1a. library_catalog['Book 1'] ==> 'A Tale of Two Cities'
# 1b. However, if you access a key that isn't present in the doctionary ==> KeyError

# 2a. book1 = library_catalog.get('book 1')
#     print(book1) ==> Output: 'A Tale of Two Cities
# 2b. book4 = library_catalog.get('book 4)
#     print(book4) ==> Output: None 


book1 = library_catalog.get('book 1')
book4 = library_catalog.get('book 4')
print(book1)
print(book4)

# Update the value of a book:
library_catalog['book 3'] = 'Diary of a Wimpy Kid'

# All methods: items(), keys(), values(), loops

all_books = library_catalog.items()
# Output: dict_items([('book1', 'A Tale of Two Cities'), ('book2', 'To Kill a Mockingbird'), ('book3', '1984')])

all_keys = library_catalog.keys()
# Output: dict_keys(['book 1', 'book 2', 'book 3'])

for key, value in library_catalog.items():
    print(key, ":", value)
