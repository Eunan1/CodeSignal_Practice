# HashMap to hold the library system
library_system = {}

# Example: Adding a book
library_system['978-3-16-148410-0'] = {'title': 'The Little Prince', 'author': 'Antoine de Saint-Exupéry', 'copies': 3}

# Example: Borrowing a book (decrementing the number of copies)
if library_system['978-3-16-148410-0']['copies'] > 0:
    library_system['978-3-16-148410-0']['copies'] -= 1  # Assuming the book is available
    print('1 copy removed from inventory')
else:
    print('Not enough copies available')