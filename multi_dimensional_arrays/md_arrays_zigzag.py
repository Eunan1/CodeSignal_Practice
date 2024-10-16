matrix1 = [
    # Cols
    [1, 2, 3, 4],
    [5, 6, 7, 8],   # Rows
    [9, 10, 11, 12]
]


# Create a function to zigzag through this matrix
# Start at bottom right go up then left then down then left then up

# Sequence: 12 -> 8 -> 4 -> 3 -> 7 -> 11 -> 10 -> 6 -> 2 -> 1 -> 5 -> 9


def desired_traversal(matrix):

    rows, cols = len(matrix), len(matrix[0]) # Dimensions
    direction = 'up' # Direction flag
    row, col = rows - 1, cols - 1 # Starting index
    output = [] 

    while len(output) < rows * cols:

        output.append(matrix[row][col])

        if direction == 'up':
            if row - 1 < 0:
                direction = 'down'
                col -= 1
            
            else:
                row -= 1
        
        else:
            if row + 1 == rows:
                direction = 'up'
                col -= 1
            else:
                row += 1
        
    return(output)


ans = desired_traversal(matrix1)
print(ans)
            





