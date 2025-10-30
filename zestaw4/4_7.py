# ZADANIE 4.7---------------------------------------------------------

def flatten(sequence):
    L=[]
    for el in sequence:
        if isinstance(el, (tuple, list)):
            L.extend(flatten(el))
        else:
            L.append(el)
    return L



seq_1 = [1,(2,3),[],[4,(5,6,7)],8,[9]]
seq_2 =[1, [[9]], ([(1,9),1]), 9, [1]] 
seq_3 = [1, [[[[(5)]],6]], (1,[((5), 6)]), 1]

assert flatten(seq_1) == [1,2,3,4,5,6,7,8,9]
assert flatten(seq_2) == [1,9,1,9,1,9,1]
assert flatten(seq_3) == [1,5,6,1,5,6,1]