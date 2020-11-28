def solve(problem):
    solution = [[1,2,3,4,5,6,7,8,9],
                [4,5,6,7,8,9,1,2,3],
                [7,8,9,1,2,3,4,5,6],
                [2,3,1,5,6,4,8,9,7],
                [5,6,4,8,9,7,2,3,1],
                [8,9,7,2,3,1,5,6,4],
                [3,1,2,6,4,5,9,7,8],
                [6,4,5,9,7,8,3,1,2],
                [9,7,8,3,1,2,6,4,5]]
    return solution

def get_row(problem,row):
    return problem[row]

def get_column(problem, column):       
        col = [row[column] for row in problem]
        return col

def get_box(problem, box):
    start = {
            1:(0,0), 2:(0,3), 3:(0,6),
            4:(3,0), 5:(3,3), 6:(3,6),
            7:(6,0), 8:(6,3), 9:(6,6)
            }
    coords = start.get(box)
    box_cube = [[problem[x][y] for y in range(coords[1], coords[1]+3)] for x in range(coords[0], coords[0]+3)]
    return box_cube

def get_box_flat(box):
    return [x for row in box for x in row]

