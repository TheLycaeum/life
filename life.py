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

def birth(board, row, col):
    board[row][col] = True

def num_live_neighbours(board, row, col):
    size = len(board)-1
    if row == 0 and col == 0:
        return int(board[0][1]) + int(board[1][1]) + int(board[1][0])
    if row == 0 and col == size:
        return int(board[0][size-1]) + int(board[1][size-1]) + int(board[1][size])
    
        
    
# neighbours
# keep_alive

# if alive(cell)

