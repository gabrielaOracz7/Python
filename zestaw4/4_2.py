# ZADANIE 4.2 -------------------------------------------------------------

def make_ruler(n):
    if n<=0 or not isinstance(n, int):
        raise ValueError('Argument must be a positive integer.')
    ruler="|"+"....|"* n
    numbers="0"
    numbers+="".join(str(i).rjust(5) for i in range(1,n+1))
    ruler=ruler+"\n"+numbers
    return ruler

assert make_ruler(8) == '|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8'
assert make_ruler(12) == '|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12'



def make_grid(rows, cols):
    if cols<=0 or rows<=0 or not isinstance(cols, int) or not isinstance(rows, int):
        raise ValueError('Number of columns/rows must be a positive integer')
    horizontal="+"+"---+" * cols
    vertical="|"+"   |" * cols
    created_grid=horizontal+("\n"+vertical+"\n"+horizontal)*rows
    return created_grid

assert make_grid(3,2) =='+---+---+\n|   |   |\n+---+---+\n|   |   |\n+---+---+\n|   |   |\n+---+---+'
assert make_grid(1,3) == '+---+---+---+\n|   |   |   |\n+---+---+---+'