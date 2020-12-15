start = {
        1:(0,0), 2:(0,3), 3:(0,6),
        4:(3,0), 5:(3,3), 6:(3,6),
        7:(6,0), 8:(6,3), 9:(6,6)
        }
baseline = {1,2,3,4,5,6,7,8,9}

test = [
        ['.',2,3,4,5,6,7,8,9],
        [4,5,6,7,'.',9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,1,5,6,4,8,9,7],
        [5,6,4,'.','.',7,2,3,1],
        [8,9,7,2,3,1,5,6,4],
        [3,1,2,6,4,5,9,7,8],
        [6,4,5,9,7,8,3,1,2],
        [9,7,8,3,1,2,6,4,5]]

example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

class Sudoku(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] not in baseline:
                    self.puzzle[row][col] = -1

    def __str__(self):
        return f"{[row for row in self.puzzle]}"

    def check_row(self, row, guess):
        # print(f"Guess: {guess}, Row: {self.puzzle[row]}")
        return guess in self.puzzle[row]
    
    def check_column(self, column, guess):
        return guess in [row[column] for row in self.puzzle]

    def check_box(self, row, column, guess):
        box_cube = [[self.puzzle[x][y] for y in range(column//3*3, column//3*3+3)] for x in range(row//3*3, row//3*3+3)]
        return guess in [x for row in box_cube for x in row]

    def is_valid(self, row, column, guess):
        # print("Inside is_valid()")
        if self.check_row(row, guess):
            return False
        
        if self.check_column(column, guess):
            return False
        
        if self.check_box(row, column, guess):
            return False
        return True

    def find_next_empty(self):
        for r in range(9):
            for c in range(9):
                # print(f"puzzle[{r}][{c}] = {self.puzzle[r][c]}")
                if self.puzzle[r][c] == -1:
                    return r,c
        return None, None
    
    def solve_sudoku(self):
        row, col = self.find_next_empty()
        # print(f"Current - Row: {row}, Col: {col}")

        if row is None:
            return True
        
        for guess in range(1,10):
            if self.is_valid(row, col, guess):
                # print(f"Row: {row}, Col: {col}, Guess: {guess}")
                self.puzzle[row][col] = guess

                if self.solve_sudoku():
                    return True
            self.puzzle[row][col] = -1
        return False
    






# def solve(problem):
#     changed = True
#     working = problem.copy()
#     while changed:
#         changed = False
#         for i in range(1,10):
#             options = get_options(working, i)
#             working, changed = implement_options(working, i, options, changed)
#             print(changed)
#     solution = working.copy()
#     return solution

# def get_row(problem,row):
#     return problem[row]

# def get_column(problem, column):       
#         col = [row[column] for row in problem]
#         return col

# def get_box(problem, box):
#     coords = start.get(box)
#     box_cube = [[problem[x][y] for y in range(coords[1], coords[1]+3)] for x in range(coords[0], coords[0]+3)]
#     return box_cube

# def get_box_flat(box):
#     return [x for row in box for x in row]

# def get_options(problem, box):
#     coords = start.get(box)
#     box = get_box(problem,box)

#     row_start = coords[0]
#     col_start = coords[1]

#     options = {}
#     for x in range(3):
#         for y in range(3):
#             row_num = row_start + x
#             col_num = col_start + y
#             if problem[row_num][col_num] not in baseline:
#                 row_values = get_row(problem, row_num)
#                 col_values = get_column(problem, col_num)
#                 box_values = get_box_flat(box)
#                 not_taken = baseline.difference(set(row_values+col_values+box_values))
#                 if len(not_taken) > 0:
#                     options[(row_num,col_num)] = not_taken
#     return options

# def implement_options(problem, box, options, changed):
#     working = problem.copy()
#     x,y = start.get(box)
#     rows = [get_row(problem, i) for i in range(x,x+3)]
#     cols = [get_column(problem, i) for i in range(y, y+3)]

#     for option in options:
#         x, y = option
#         values = list(options[option])
#         print(f"options: {option}")
#         print(f"values: {values}")

#         if working[x][y] in baseline:
#             print("Number already filled in")
#         elif len(values) == 1:
#             working[x][y] = values[0]
#             changed = True
#             print(f"Inserted {value} in ({x},{y})")
#             print(f"x: {x}, y: {y}, values: {values[0]}")
#         elif len(values) > 1:
#             print("Check for possible")
#             other_r = [rows[i] for i in range(3) if i != x%3]
#             other_c = [cols[i] for i in range(3) if i != y%3]
#             other = other_r + other_c
#             for value in values:
#                 print(value)
#                 print(other)
#                 if all([value in group for group in other]):
#                     working[x][y] = values[0]
#                     changed = True
#                     print(f"Inserted {value} in ({x},{y})")
#                     print(f"x: {x}, y: {y}, values: {values[0]}")
#         else:
#             print(f"Couldnt insert {value} in ({x},{y})")
        
#     return working, changed

