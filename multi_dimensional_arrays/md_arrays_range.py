matrix = [
        # Cols
    [1, 2, 3, 4],
    [5, 6, 7, 8],   # Rows
    [9, 10, 11, 12]
]


def reverse_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    output = []

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            output.append(matrix[row][col])
    
    return output

ans = reverse_traverse(matrix)
print(ans)