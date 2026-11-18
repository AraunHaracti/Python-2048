from field import Field


def print_field(field):
    print("-" * 20)
    for row in field:
        for cell in row:
            print(cell, end="\t")
        print()
    print("-" * 20)


if __name__ == "__main__":
    width = int(input("Width: "))

    field = Field(width, print_field)

    field.print_field()

    while True:
        direction = input("up, down, left, right: ")

        field.shift(direction)

        field.print_field()
