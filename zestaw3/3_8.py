# ZADANIE 3.8 ----------------------------------------------------------------------

def analyze_sequences(first_seq, second_seq):
    set1=set(first_seq)
    set2=set(second_seq)
    common_el= list(set1 & set2)
    all_unique_el= list(set1 | set2)
    
    common_el.sort()
    all_unique_el.sort()
    return common_el, all_unique_el


seq1="abcde"
seq2="ijkamd"
assert analyze_sequences(seq1,seq2) == (['a', 'd'], ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'k', 'm']) #([common_el],   [all_unique_el])

seq1=[1,2,3,4,5,6,7,8,9]
seq2=[2,4,6,8,10,12]
assert analyze_sequences(seq1, seq2) == ([2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])

seq1="a12b34c"
seq2="ef90bc54"
assert analyze_sequences(seq1, seq2) == (['4', 'b', 'c'], ['0', '1', '2', '3', '4', '5', '9', 'a', 'b', 'c', 'e', 'f'])

