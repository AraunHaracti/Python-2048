from random import choice


class Field:

    def __init__(self, width, method_print_field):
        self.method_print_field = method_print_field
        self.width = width

        self.field = [[0 for j in range(self.width)] for i in range(self.width)]
        
        self.rand_add_an_item(2)


    def rand_add_an_item(self, element):
        zero_cells = list()
        
        for i in range(self.width):
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zero_cells.append((i, j))
    
        coord_cell = choice(zero_cells)
    
        self.field[coord_cell[0]][coord_cell[1]] = element


    def __change_direction(self, direction: str):
        match direction:
            case "up":
                self.field = [[self.field[j][i] for j in range(self.width)] for i in range(self.width)]
            case "left":
                self.field = self.field
            case "right":
                self.field = [[self.field[i][self.width - 1 - j] for j in range(self.width)] for i in range(self.width)]
            case "down":
                self.field = [[self.field[self.width - 1 - j][self.width - 1 - i] for j in range(self.width)] for i in range(self.width)]


    def shift(self, direction):

        self.__change_direction(direction)

        for row in self.field:
            for i in range(self.width):
                for j in range(self.width - 1 - i):
                    if row[j] == 0:
                        row[j], row[j+1] = row[j+1], row[j]

            for j in range(self.width - 1):   
                if row[j] == row[j+1]:
                    row[j], row[j+1] = row[j] * 2, 0

            for i in range(self.width):
                for j in range(self.width - 1 - i):
                    if row[j] == 0:
                        row[j], row[j+1] = row[j+1], row[j]

        self.__change_direction(direction)

        self.rand_add_an_item(2)


    def print_field(self):
        self.method_print_field(self.field)

    