matrix = [
    [1, 2, 3, 4],
    [5, 6, 7 ,8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def secondary_diagonal_transpos(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    output = []

    for i in range(rows):
        for j in range(cols):
            output[cols - j - 1][rows - i -1] = matrix[i][j]

    return output