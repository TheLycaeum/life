import life

def test_display_all_dead_3x3():
    board = [[False, False, False],
             [False, False, False],
             [False, False, False]]
    val = life.display(board)
    assert val == "...\n...\n..."

def test_display_all_dead_4x4():
    board = [[False, False, False, False],
             [False, False, False, False],
             [False, False, False, False],
             [False, False, False, False]]
    val = life.display(board)
    assert val == "....\n....\n....\n...."

    
def test_display_add_alive_3x3():
    board = [[True, True, True],
             [True, True, True],
             [True, True, True]]
    val = life.display(board)
    assert val == "XXX\nXXX\nXXX"
    

def test_display_random_3x3():
    board = [[True, False, True],
             [False, True, False],
             [True, False, True]]
    val = life.display(board)
    assert val == "X.X\n.X.\nX.X"


def test_alive_dead():
    board = [[True, True, True],
             [True, True, False],
             [True, True, True]]
    val = life.alive(board, 1,2)
    assert val == False

def test_alive_alive():
    board = [[False, False, False],
             [False, False, True],
             [False, False, False]]
    val = life.alive(board, 1,2)
    assert val == True


def test_kill():
    board = [[False, False, False],
             [False, False, True],
             [False, False, False]]
    assert board[1][2] == True
    life.kill(board, 1, 2)
    assert board[1][2] == False

def test_kill2():
    board = [[True, True],
             [True, True]]
    assert board[0][0] == True
    life.kill(board, 0, 0)
    assert board[0][0] == False

def test_birth():
    board = [[False, False, False],
             [False, False, False],
             [False, False, False]]
    assert board[1][2] == False
    life.birth(board, 1, 2) 
    assert board[1][2] == True

def test_num_live_neighbours_tl():
    board = [[False, False, False],
             [False, True, True],
             [False, False, True]]
    val = life.num_live_neighbours(board, 0, 0)
    assert val == 1


def test_num_live_neighbours_tl2():
    board = [[False, False, False],
             [True, True, True],
             [False, False, True]]
    val = life.num_live_neighbours(board, 0, 0)
    assert val == 2

def test_num_live_neighbours_tr():
    board = [[False, False, False],
             [False, True, True],
             [False, False, True]]
    val = life.num_live_neighbours(board, 0, 2)
    assert val == 2

    
  

    

    
