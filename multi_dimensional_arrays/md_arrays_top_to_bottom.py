def vertical_traverse(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    output = []
    row, col = (rows - 1), (cols - 1)

    while len(output) < rows * cols:

        output.append(matrix[row][col])

        if row - 1 < 0:
            col -= 1
            row += 2
        else:
            row -= 1

    return output    


# Example matrix representing library bookshelves
bookshelves = [
        # Col
    [1, 2, 3, 4],
    [5, 6, 7, 8],   # Row
    [9, 10, 11, 12]
]

# Output should be the vertical traverse of the bookshelves
print(vertical_traverse(bookshelves))  # [12, 8, 4, 11, 7, 3, 10, 6, 2, 9, 5, 1]