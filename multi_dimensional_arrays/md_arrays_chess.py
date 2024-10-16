def find_positions(board):
    
    rows, cols = len(board), len(board[0])
    row, col = (rows - 1), (cols - 1)
    

    positions = []

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "E":
                if (
                    # Checks we're not at the first row and checks the previous row for 'E'
                    (row > 0 and board[i-1][j] == "E") or
                    # Checks we're not at the last row and checks the next row for 'E'
                    (i < row and board[i+1][j] == "E") or
                    # Checks we're not at the first column and checks previous columns for 'E'
                    (col > 0 and board[i][j-1] == "E") or
                    # Checks we're not at the 
                    (j < col and board[i][j+1] == "E")
                ):
                    positions.append((i, j))
    
    return positions

board = [
          # Col
    ['P', 'E', 'E', 'P'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'P'],  # Row
    ['P', 'E', 'P', 'E']
]

ans = find_positions(board)
print(ans)