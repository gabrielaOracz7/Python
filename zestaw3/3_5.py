# ZADANIE 3.5----------------------------------------------------------------------

def draw_a_ruler(length):
    if  length<=0:
        raise ValueError('Wrong input - length must be a positive integer.')
    ruler="|"+"....|"*length
    numbers="0"
    numbers+="".join(str(i).rjust(5) for i in range(1,length+1))
    ruler=ruler+"\n"+numbers
    return ruler

assert draw_a_ruler(11)=="|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11"
