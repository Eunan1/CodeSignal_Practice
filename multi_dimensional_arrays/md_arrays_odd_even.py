# Initial method: 
# Travel Even-indexed columns upwards
# Travel Odd-indexed columns downwards
# Reverse this pattern

def print_book_traversal(bookshelves):
    rows = len(bookshelves)
    cols = len(bookshelves[0])
    for col in range(cols-1, -1, -1):
        if col % 2 == 0:
            for row in range(rows):
                print(bookshelves[row][col], end=" ")
        else:
            for row in range(rows-1, -1, -1):
                print(bookshelves[row][col], end=" ")
                
if __name__ == "__main__":
    bookshelves = [[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]]
    print_book_traversal(bookshelves)