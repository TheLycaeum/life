import time

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
    size = len(board) - 1
    num = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            nx, ny = row + x, col + y
            if x == 0 and y == 0:
                continue
            if nx < 0 or nx > size:
                continue
            if ny < 0 or ny > size:
                continue
            num += int(board[nx][ny])
    return num
            

def create_new_board(size):
    ret = []
    for i in range(size):
        cols = []
        for j in range(size):
            cols.append(False)
        ret.append(cols)
    return ret

        
def apply_rules(board):
    ret_board = create_new_board(len(board))
    # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.

    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    for row in range(len(board)):
        for col in range(len(board)):
            if alive(board, row, col) and num_live_neighbours(board, row, col) < 2:
                kill(ret_board, row, col)
            if alive(board, row, col) and num_live_neighbours(board, row, col) in [2,3]:
                birth(ret_board, row, col)
            if not alive(board, row, col) and num_live_neighbours(board, row, col) == 3:
                birth(ret_board, row, col)

    return ret_board
                

def main():
    board = [[False, True, False, False],
             [False, True, False, False],
             [False, True, False, True],
             [False, False, True, False]]

    count = 1
    while True:
        print (count)
        print (display(board))
        board = apply_rules(board)
        time.sleep(1)
        count += 1

if __name__ == "__main__":
    main()
