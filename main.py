from time import perf_counter

list1 = ['computer', 'Richie', 'linux', 'each', 'night', 'notebook', 'keyboard', 'mouse', 'javascript', 'python', 'java', 'kotlin']
list2 = ['smartphone', 'android', 'BSD', 'Tailwind', 'Cascading', 'HyperText', 'Brave', 'postgres']
typed_all = False
TypedWord = ''
which_list = ''
correct_choose = False

while correct_choose == False:
    if which_list == '1' or which_list == '2': 
        correct_choose = True
    else:
        which_list = input('Choose what list do you want, 1 or 2: ')
        

start = perf_counter()  

while typed_all == False:
    if which_list == '1':
        print(list1)
        TypedWord = input('Type: ')
        for i in list1:
            Igual = i == TypedWord
            if Igual == True:
                list1.remove(i) 
            pass
            if not list1:
                typed_all = True
    elif which_list == '2':
        print(list2)
        TypedWord = input('Digite: ')
        for i in list2:
            Igual = i == TypedWord
            if Igual == True:
                list2.remove(i) 
            pass
            if not list2:
                typed_all = True
    

end = perf_counter() 

print(end-start)
