import pytest
import sudoku

baseline = {1,2,3,4,5,6,7,8,9}

problem = [[5,3,'_','_',7,'_','_','_','_'],
        [6,'_','_',1,9,5,'_','_','_',],
        ['_',9,8,'_','_','_','_',6,'_'],
        [8,'_','_','_',6,'_','_','_',3],
        [4,'_','_',8,'_',3,'_','_',1],
        [7,'_','_','_',2,'_','_','_',6],
        ['_',6,'_','_','_','_',2,8,'_'],
        ['_','_','_',4,1,9,'_','_',5],
        ['_','_','_','_',8,'_','_',7,9]]

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
    solution = sudoku.solve(problem)
    for row in solution:
        assert set(row) == baseline

def test_columns():
    solution = sudoku.solve(problem)
    for i in range(9):
        col = [row[i] for row in solution]
        assert set(col) == baseline

def test_boxes():
    solution = sudoku.solve(problem)
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