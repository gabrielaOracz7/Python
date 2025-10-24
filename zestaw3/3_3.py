# ZADANIE 3.3----------------------------------------------------------------------------------------------

not_divisible_by_three=[]
for i in range(31):
    if i%3: #False = 0
        not_divisible_by_three.append(i)

#print(not_divisible_by_three)
assert not_divisible_by_three == [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]
