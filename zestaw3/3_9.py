# ZADANIE 3.9----------------------------------------------------------------------

def calculate_sum_of_sequences(L):
    return [sum(seq) for seq in L]

my_list1=[[],[4],(1,2),[3,4],(5,6,7)]
assert calculate_sum_of_sequences(my_list1)==[0,4,3,7,18]

my_list2=[[2,3,4], (), (1,2), [3,3,3], [], []]
assert calculate_sum_of_sequences(my_list2)==[9,0,3,9,0,0]

