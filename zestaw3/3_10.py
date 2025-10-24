# ZADANIE 3.10-------------------------------------------------------------------------------------

def create_dictionary_1():
    my_dict={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return my_dict

def create_dictionary_2():
    my_dict=[('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
    return dict(my_dict)

def create_dictionary_3():
    roman=['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic=[1,5,10,50,100,500,1000]
    return dict(zip(roman, arabic))

def create_dictionary_4():
    my_dict={}
    roman=['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic=[1,5,10,50,100,500,1000]
    for(r,a) in zip(roman, arabic):
        my_dict[r]=a
    return my_dict

assert create_dictionary_1() == {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
assert create_dictionary_2() == {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
assert create_dictionary_3() == {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
assert create_dictionary_4() == {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


#--------------------------------------------------------------------------------------------------
def roman2int(roman):
    roman=roman.upper()
    dictionary=create_dictionary_3()
    repeat_limit={'I':3, 'V':1, 'X':3, 'L':1, 'C':3, 'D':1, 'M':3} 
    valid_substractions={
        'I' : ('V', 'X'),  # 'I' can appear only before 'V' or 'X'
        'X' : ('L', 'C'),
        'C' : ('D', 'M')
    }
   
    last_substract_symbol=""
    prev_symbol =""
    prev_prev_symbol=""
    total_value=0
    repeat_count=0
    
    for symbol in roman:
        curr_symbol_value=dictionary.get(symbol)
        if symbol not in dictionary:
            print("Invalid input: "+roman+" - Roman numeral must consist only of the characters: 'I', 'V', 'X', 'L', 'C', 'D', 'M'. ")
            return

        if symbol==prev_symbol: #e.g. XX
            repeat_count+=1
            if repeat_limit.get(symbol)<repeat_count:
                print("Invalid input: "+roman+" - Too many repetitions of: ", symbol)
                return
                
            if prev_prev_symbol and dictionary.get(prev_prev_symbol)<curr_symbol_value: #e.g. XCC
                print("Invalid input: "+roman+" - wrong combination: "+ prev_prev_symbol+prev_symbol+symbol)
                return
        else:
            repeat_count=1
       
        if  prev_symbol  and dictionary.get(prev_symbol)<curr_symbol_value:
            if prev_symbol not in valid_substractions or symbol not in valid_substractions[prev_symbol]:   #e.g. VX or IM
                print("Invalid input: "+roman+" - "+ symbol+ " can not appear after "+prev_symbol )
                return
    
            if prev_prev_symbol and curr_symbol_value>dictionary.get(prev_prev_symbol):  #e.g. VIX
                print("Invalid input: "+roman+" - wrong combination: "+ prev_prev_symbol+prev_symbol+symbol)
                return                
            last_substract_symbol=prev_symbol
            total_value=total_value-2*dictionary.get(prev_symbol)+curr_symbol_value
        else:  #when prev_symbol  > symbol
            if last_substract_symbol==symbol: #e.g. XIXI
                print('Invalid input: '+roman)
                return
                
            total_value+=curr_symbol_value
            last_substract_symbol=None
        prev_prev_symbol=prev_symbol
        prev_symbol =symbol
        
    return total_value


assert roman2int('XCC') == None
assert roman2int('III')==3
assert roman2int('MMXXV')==2025
assert roman2int('XLVIII')==48
assert roman2int('XCXCXC')==None
assert roman2int('DCCCXCIX')==899 
assert roman2int('iix')==None
assert roman2int('IIII')==None
assert roman2int('CVX')==None
assert roman2int('MDCCCXCV')==1895
assert roman2int('abc')==None

