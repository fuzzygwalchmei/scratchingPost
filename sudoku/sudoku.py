start = {
        1:(0,0), 2:(0,3), 3:(0,6),
        4:(3,0), 5:(3,3), 6:(3,6),
        7:(6,0), 8:(6,3), 9:(6,6)
        }
baseline = {1,2,3,4,5,6,7,8,9}

def solve(problem):
    changed = True
    working = problem.copy()
    while changed:
        changed = False
        for i in range(1,10):
            options = get_options(working, i)
            working, changed = implement_options(working, i, options, changed)
            print(changed)
    solution = working.copy()
    return solution

def get_row(problem,row):
    return problem[row]

def get_column(problem, column):       
        col = [row[column] for row in problem]
        return col

def get_box(problem, box):
    coords = start.get(box)
    box_cube = [[problem[x][y] for y in range(coords[1], coords[1]+3)] for x in range(coords[0], coords[0]+3)]
    return box_cube

def get_box_flat(box):
    return [x for row in box for x in row]

def get_options(problem, box):
    coords = start.get(box)
    box = get_box(problem,box)

    row_start = coords[0]
    col_start = coords[1]

    options = {}
    for x in range(3):
        for y in range(3):
            row_num = row_start + x
            col_num = col_start + y
            if problem[row_num][col_num] not in baseline:
                row_values = get_row(problem, row_num)
                col_values = get_column(problem, col_num)
                box_values = get_box_flat(box)
                not_taken = baseline.difference(set(row_values+col_values+box_values))
                if len(not_taken) > 0:
                    options[(row_num,col_num)] = not_taken
    return options

def implement_options(problem, box, options, changed):
    working = problem.copy()
    x,y = start.get(box)
    rows = [get_row(problem, i) for i in range(x,x+3)]
    cols = [get_column(problem, i) for i in range(y, y+3)]

    for option in options:
        x, y = option
        values = list(options[option])
        print(f"options: {option}")
        print(f"values: {values}")

        if working[x][y] in baseline:
            print("Number already filled in")
        elif len(values) == 1:
            working[x][y] = values[0]
            changed = True
            print(f"Inserted {value} in ({x},{y})")
            print(f"x: {x}, y: {y}, values: {values[0]}")
        elif len(values) > 1:
            print("Check for possible")
            other_r = [rows[i] for i in range(3) if i != x%3]
            other_c = [cols[i] for i in range(3) if i != y%3]
            other = other_r + other_c
            for value in values:
                print(value)
                print(other)
                if all([value in group for group in other]):
                    working[x][y] = values[0]
                    changed = True
                    print(f"Inserted {value} in ({x},{y})")
                    print(f"x: {x}, y: {y}, values: {values[0]}")
        else:
            print(f"Couldnt insert {value} in ({x},{y})")
        
    return working, changed

