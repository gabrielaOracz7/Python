# ZADANIE 3.6------------------------------------------------------------------------------

def draw_rectangle_from_the_grid(rows, columns):
    if columns<=0 or rows<=0:
        raise ValueError('Wrong input - number of columns/rows must be a positive integer')
    horizontal="+"+"---+"*columns
    vertical="|"+"   |"*columns
    created_grid=horizontal+("\n"+vertical+"\n"+horizontal)*rows
    return created_grid

#print(draw_rectangle_from_the_grid(2,4))
assert draw_rectangle_from_the_grid(2,4)== "+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+\n|   |   |   |   |\n+---+---+---+---+"
