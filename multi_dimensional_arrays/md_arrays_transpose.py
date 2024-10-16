matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    output = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            output[j][i] = matrix [i][j]

    return output

def transpose_shorthand(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    output = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return output

ans1 = transpose_matrix(matrix)
ans2 = transpose_shorthand(matrix)

print(ans1)
print("\n")
print(ans2)