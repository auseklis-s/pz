N=int(input("Введите целое число N:"))
K=1
if type(N)==int and N>0:
    while K**2 <= N:
        K +=1
        print(K)    

    
