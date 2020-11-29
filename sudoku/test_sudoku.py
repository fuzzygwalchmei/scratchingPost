import pytest
import sudoku

baseline = {1,2,3,4,5,6,7,8,9}

problem = [
        ['.',2,3,4,5,6,7,8,9],
        [4,5,6,7,'.',9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,1,5,6,4,8,9,7],
        [5,6,4,'.','.',7,2,3,1],
        [8,9,7,2,3,1,5,6,4],
        [3,1,2,6,4,5,9,7,8],
        [6,4,5,9,7,8,3,1,2],
        [9,7,8,3,1,2,6,4,5]]

real_problem = [
    [7,'.','.','.','.',1,'.','.','.'],
    ['.','.','.',2,'.','.',3,'.','.'],
    ['.',9,'.',4,'.','.','.',7,1],
    [8,'.','.','.','.',4,5,3,'.'],
    ['.','.','.',6,'.',8,'.','.','.'],
    ['.',3,1,5,'.','.','.','.',9],
    [4,7,'.','.','.',5,'.',6,'.'],
    ['.','.',8,'.','.',6,'.','.','.'],
    ['.','.','.',1,'.','.','.','.',7]]
}

solution = [[1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,1,5,6,4,8,9,7],
            [5,6,4,8,9,7,2,3,1],
            [8,9,7,2,3,1,5,6,4],
            [3,1,2,6,4,5,9,7,8],
            [6,4,5,9,7,8,3,1,2],
            [9,7,8,3,1,2,6,4,5]]

def test_rows():
    for row in solution:
        assert set(row) == baseline

def test_columns():
    for i in range(9):
        col = [row[i] for row in solution]
        assert set(col) == baseline

def test_boxes():
    start = {
            1:(0,0), 2:(0,3), 3:(0,6),
            4:(3,0), 5:(3,3), 6:(3,6),
            7:(6,0), 8:(6,3), 9:(6,6)
            }
    for i in start.keys():
        coords = start.get(i)
        box_cube = [[solution[x][y] for y in range(coords[1], coords[1]+3)] for x in range(coords[0], coords[0]+3)]
        box_flat = [x for row in box_cube for x in row]
        assert set(box_flat) == baseline

@pytest.mark.parametrize('problem, row, answer', 
                        [(solution, 0, [1,2,3,4,5,6,7,8,9]),
                        (solution, 3, [2,3,1,5,6,4,8,9,7])])
def test_get_row(problem, row, answer):
    test_row = sudoku.get_row(problem, row)
    assert test_row == answer


@pytest.mark.parametrize('problem, col, answer', 
                        [(solution, 0, [1,4,7,2,5,8,3,6,9]),
                        (solution, 3, [4,7,1,5,8,2,6,9,3])])
def test_get_column(problem, col, answer):
    test_col = sudoku.get_column(problem, col)
    assert test_col == answer

@pytest.mark.parametrize('problem, box, answer', 
                        [(solution, 1, [[1,2,3],[4,5,6],[7,8,9]]),
                        (solution, 7, [[3,1,2,],[6,4,5],[9,7,8]])])
def test_get_box(problem, box, answer):
    test_box = sudoku.get_box(problem, box)
    assert test_box == answer
        

@pytest.mark.parametrize('problem, box, answer', 
                        [(solution, 1, [1,2,3,4,5,6,7,8,9]),
                        (solution, 7, [3,1,2,6,4,5,9,7,8])])
def test_get_box_flat(problem, box, answer):
    test_box = sudoku.get_box(problem, box)
    test_flat = sudoku.get_box_flat(test_box)
    assert test_flat == answer

@pytest.mark.parametrize('box, answer', 
                        [(1, {(0,0):{1}}),
                        (5, {(4,3):{8},
                            (4,4):{8,9}
                            })])
def test_get_options(box, answer):

    test_opt = sudoku.get_options(problem, box)
    assert test_opt == answer

@pytest.mark.parametrize('options, answer', 
                        [({(0,0):{1}}, 
                        [
                        [1,2,3,4,5,6,7,8,9],
                        [4,5,6,7,'.',9,1,2,3],
                        [7,8,9,1,2,3,4,5,6],
                        [2,3,1,5,6,4,8,9,7],
                        [5,6,4,'.','.',7,2,3,1],
                        [8,9,7,2,3,1,5,6,4],
                        [3,1,2,6,4,5,9,7,8],
                        [6,4,5,9,7,8,3,1,2],
                        [9,7,8,3,1,2,6,4,5]]),
                        ({(4,3):{8},
                        (4,4):{8,9}
                        }, 
                        [
                        [1,2,3,4,5,6,7,8,9],
                        [4,5,6,7,'.',9,1,2,3],
                        [7,8,9,1,2,3,4,5,6],
                        [2,3,1,5,6,4,8,9,7],
                        [5,6,4,8,'.',7,2,3,1],
                        [8,9,7,2,3,1,5,6,4],
                        [3,1,2,6,4,5,9,7,8],
                        [6,4,5,9,7,8,3,1,2],
                        [9,7,8,3,1,2,6,4,5]])
                        ])
def test_implement_options(options, answer):
    test_problem = problem.copy()
    actual = sudoku.implement_options(test_problem, options)
    assert answer == actual

def test_solve():
    actual = sudoku.solve(problem)
    assert actual == solution