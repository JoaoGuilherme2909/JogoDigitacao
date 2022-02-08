from time import perf_counter

lista1 = ['computer', 'each', 'night', 'notebook', 'keyboard', 'mouse', 'javascript', 'python']
digitou_todas = False
palavraDigitada = ''

start = perf_counter()  

while digitou_todas == False:
    print(lista1)
    palavraDigitada = input('Digite: ')
    for i in lista1:
       Igual = i == palavraDigitada
       if Igual == True:
            lista1.remove(i) 
       else:
           pass
       pass
    if not lista1:
        digitou_todas = True
        pass
    pass

end = perf_counter() 

print(end-start)
