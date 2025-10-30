# ZADANIE 4.5-------------------------------------------------------------------------------------

def odwracanie_iteracyjnie(L, left, right):
    l=left
    r=right
    while l<r:
        L[l], L[r] = L[r], L[l]
        l+=1
        r-=1


def odwracanie_rekurencyjnie(L, left, right):
    if left>=right:
        return
    L[left], L[right] = L[right], L[left]
    odwracanie_rekurencyjnie(L, left+1, right-1)




#        (function_to_test,    original_list,   left_index,   right_index,   list_after_reverse)
test_data = [ (odwracanie_iteracyjnie, [0,1,2,3,4,5,6,7,8,9], 2, 5, [0,1, 5, 4, 3, 2, 6, 7, 8, 9]), 
         (odwracanie_iteracyjnie, [1,3,5,7,9], 0, 1, [3,1,5,7,9]),
         (odwracanie_rekurencyjnie, [0, 2 ,4 ,6, 8], 1, 4, [0, 8, 6, 4, 2] ), 
         (odwracanie_rekurencyjnie, [1,2,3,4,5,4,3,2,1], 4, 8, [1,2, 3, 4, 1, 2, 3, 4, 5])  ]

for funct, my_list, left, right, result in test_data:
    funct(my_list, left, right)
    assert my_list == result 

