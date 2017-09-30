import life

def test_display_all_dead_3x3():
    board = [[False, False, False],
             [False, False, False],
             [False, False, False]]
    val = life.display(board)
    assert val == "...\n...\n..."

    
