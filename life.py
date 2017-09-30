def display(board):
    ret = []
    for row in board:
        t_row = []
        for col in row:
            if col:
                t_row.append("X")
            else:
                t_row.append(".")
        ret.append("".join(t_row))
    return "\n".join(ret)
        

def alive(board, row, col):
    return board[row][col]

def kill(board, row, col):
    board[row][col] = False
    
# kill
# birth
# neighbours
# keep_alive

# if alive(cell)
