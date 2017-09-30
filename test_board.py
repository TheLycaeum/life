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
    
