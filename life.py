def display(board):
    if board[0][0]:
        char = "X"
    else:
        char = "."
    
    size = len(board)
    row = char*size
    disp = "\n".join([row] * size)
    return disp
        
        
