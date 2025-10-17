#ZADANIE 2.10-------------------------------------------------
line="Lorem ipsum GvRdolor sit amet\n  GvR consectetur\t adipiscing GvR\n elit laGvRoreet\t arcu\n libero"
list_of_words=line.split()
number_of_words=len(list_of_words)

assert number_of_words==13

#ZADANIE 2.11-------------------------------------------------
word='abcdefg'
new_word="_".join(word)

assert new_word=='a_b_c_d_e_f_g'

#ZADANIE 2.12-------------------------------------------------
first_letters="".join(el[0] for el in list_of_words)
last_letters="".join(el[-1] for el in list_of_words)

assert first_letters=='LiGsaGcaGelal'
assert last_letters=='mmrttRrgRttuo'

#ZADANIE 2.13-------------------------------------------------
total_length=sum(len(x) for x in list_of_words)

assert total_length==76

#ZADANIE 2.14-------------------------------------------------
the_longest_word=max(list_of_words, key=len)
len_of_the_longest=len(the_longest_word)

assert the_longest_word=='consectetur'
assert len_of_the_longest==11

#ZADANIE 2.15-------------------------------------------------
L=[1, 11,22,334,45,566,778, 8, 9, 90]
string_with_numbers="".join(str(el) for el in L)

assert string_with_numbers=='11122334455667788990'

#ZADANIE 2.16-------------------------------------------------
new_line=line.replace("GvR", "Guido van Rossum")

assert new_line=='Lorem ipsum Guido van Rossumdolor sit amet\n  Guido van Rossum consectetur\t adipiscing Guido van Rossum\n elit laGuido van Rossumoreet\t arcu\n libero'

#ZADANIE 2.17-------------------------------------------------
sorted_by_alpha=sorted(list_of_words, key=str.lower)
sorted_by_length=sorted(list_of_words, key=len) #sortowanie rosnąco

assert sorted_by_alpha==['adipiscing', 'amet', 'arcu', 'consectetur', 'elit', 'GvR', 'GvR', 'GvRdolor', 'ipsum', 'laGvRoreet', 'libero', 'Lorem', 'sit']
assert sorted_by_length==['sit', 'GvR', 'GvR', 'amet', 'elit', 'arcu', 'Lorem', 'ipsum', 'libero', 'GvRdolor', 'adipiscing', 'laGvRoreet', 'consectetur']

#ZADANIE 2.18-------------------------------------------------
big_number=12003000040
zeros_count=str(big_number).count("0")

assert zeros_count==7

#ZADANIE 2.19-------------------------------------------------
three_digit_blocks="".join(str(el).zfill(3) for el in L)

assert three_digit_blocks=='001011022334045566778008009090'
