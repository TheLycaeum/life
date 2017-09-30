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

def test_num_live_neighbours_bl():
    board = [[False, False, False],
             [False, True, True],
             [False, False, True]]
    val = life.num_live_neighbours(board, 2, 0)
    assert val == 1

def test_num_live_neighbours_br():
    board = [[False, False, False],
             [False, True, True],
             [False, False, True]]
    val = life.num_live_neighbours(board, 2, 2)
    assert val == 2
    
def test_num_live_neighbours_t():
    board =[[False, False, False],
            [False, True, True],
            [False, False, True]]
    val = life.num_live_neighbours(board, 0, 1)
    assert val == 2

    
def test_num_live_neighbours_l():
    board =[[True, False, False],
            [False, True, True],
            [True, True, True]]
    val = life.num_live_neighbours(board, 1, 0)
    assert val == 4

def test_num_live_neighbours_l2():
    board =[[True, False, False, True],
            [True, True, True,  False],
            [False, True, True, False],
            [True, True, True, True]]
    val = life.num_live_neighbours(board, 2, 0)
    assert val == 5


def test_num_live_neighbours_b():
    board =[[True, False, False, True],
            [True, True, True,  False],
            [False, True, True, False],
            [True, True, True, True]]
    val = life.num_live_neighbours(board, 3, 1)
    assert val == 4

def test_num_live_neighbours_r():
    board =[[True, False, False, True],
            [True, True, True,  False],
            [False, True, True, False],
            [True, True, True, True]]
    val = life.num_live_neighbours(board, 1, 3)
    assert val == 3

def test_num_live_neighbours_c():
    board =[[True, False, False, True],
            [True, True, True,  False],
            [False, True, True, False],
            [True, True, True, True]]
    val = life.num_live_neighbours(board, 2, 2)
    assert val == 6

    
def test_create_new_board():
    board =[[True, False, False, True],
            [True, True, True,  False],
            [False, True, True, False],
            [True, True, True, True]]
    val = life.create_new_board(len(board))
    assert val == [[False, False, False, False],
                   [False, False, False, False],
                   [False, False, False, False],
                   [False, False, False, False]]

    
def test_apply_rules_rule1():
    # Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    board = [[True, True, True],
             [False, False, False],
             [False, False, False]]
    assert life.alive(board, 0, 0)
    board = life.apply_rules(board)
    assert not life.alive(board, 0, 0)
    

def test_apply_rules_rule2_2_live_neighbours():
    # Any live cell with two or three live neighbours lives on to the next generation.    
    board = [[True, True, True],
             [False, False, False],
             [False, False, False]]
    assert life.alive(board, 0, 1)
    board = life.apply_rules(board)
    assert life.alive(board, 0, 1)

def test_apply_rules_rule2_3_live_neighbours():
    # Any live cell with two or three live neighbours lives on to the next generation.   
    board = [[True, True, True],
             [False, True, False],
             [False, False, False]]
    assert life.alive(board, 0, 1)
    board = life.apply_rules(board)
    assert life.alive(board, 0, 1)

