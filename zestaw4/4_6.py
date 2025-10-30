# ZADANIE 4.6----------------------------------------------------

def sum_seq(sequence):
    total=0
    for el in sequence:
        if isinstance(el, (list, tuple)):
            total+=sum_seq(el)
        else:
            total+=el
    return total



seq_1 = [1,(2,3),[],[4,(5,6,7)],8,[9]]
seq_2 =[1, [[9]], ([(1,9),1]), 9, [1]] 
seq_3 = [1, [[[[(5)]],6]], (1,[((5), 6)]), 1]


assert sum_seq(seq_1) == 45
assert sum_seq(seq_2) == 31
assert sum_seq(seq_3) == 25