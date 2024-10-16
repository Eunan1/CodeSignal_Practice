# Create a method to check for 3 * 3 subarrays within a given array

def find_subarrays(matrix):

    rows, cols = len(matrix), len(matrix[0])
    row, col = (rows - 1), (cols - 1)
    count = 0

    for i in range(rows - 2):
        for j in range(cols - 2):
            if (
                (matrix[i][j] == "E") and
                (matrix[i+2][j] == "E") and
                (matrix[i][j+2] == "E") and
                (matrix[i+2][j+2] == "E")
            ):
                count += 1
            else:
                continue
    
    return count
                

            
board = [
          # Col
    ['P', 'E', 'E', 'P', 'E'],
    ['E', 'P', 'P', 'E', 'P'],
    ['P', 'E', 'E', 'P', 'E'],  # Row
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'P', 'E', 'P', 'E']
]



ans = find_subarrays(board)
print(ans)