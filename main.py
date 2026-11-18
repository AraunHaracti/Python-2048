from random import choice
from math import floor

def generat_field(width: int):
    field = [[0 for j in range(width)] for i in range(width)]

    field = rand_cell_field(field, 2)
    field = rand_cell_field(field, 2)

    return field

def rand_cell_field(field: list[int, int], item):
    width = len(field)

    zero_cells = list()

    for i in range(width):
        for j in range(width):
            if field[i][j] == 0:
                zero_cells.append((i, j))

    coord_cell = choice(zero_cells)

    field[coord_cell[0]][coord_cell[1]] = item

    return field


def print_field(field):
    print("-" * 20)
    for row in field:
        for cell in row:
            print(cell, end="\t")
        print()
    print("-" * 20)

def change_direction(field: list[int, int], direction: str):
    width = len(field)

    match direction:
        case "up":
            return [[field[j][i] for j in range(width)] for i in range(width)]
        case "left":
            return field
        case "right":
            return [[field[i][width - 1 - j] for j in range(width)] for i in range(width)]
        case "down":
            return [[field[width - 1 - j][width - 1 - i] for j in range(width)] for i in range(width)]


def shift(field: list[int, int], direction="left"):

    width = len(field)
    
    field = change_direction(field, direction)

    for row in field:
        for i in range(width - 1):
            for j in range(width - 1 - i):
                if row[j] == 0:
                    row[j], row[j+1] = row[j+1], row[j]

        for j in range(width - 1):   
            if row[j] == row[j+1]:
                row[j], row[j+1] = row[j] * 2, 0

        for i in range(width - 1):
            for j in range(width - 1 - i):
                if row[j] == 0:
                    row[j], row[j+1] = row[j+1], row[j]

    field = change_direction(field, direction)

    field = rand_cell_field(field, 2)

    return field


width = int(input("Width: "))

field = generat_field(width)

print_field(field)

while True:
    direction = input("up, down, left, right: ")

    field = shift(field, direction)

    print_field(field)
