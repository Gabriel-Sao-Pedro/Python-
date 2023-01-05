x = -2 
n = 0
f = 63
c = 0
while(x != -1):
    x = int(input('Digite um número entre 1 e 64 meu consagrado \n'))
    z = x
    v = x
    if(x >= 1 and x <= 64):
        n = 10**(x-1) + n
        print(n) 
    if (c > x):
        z = 64
    while(c < z):
        v = v % 2
        c+= 1
    if (v > 1):
         print("Número repetido. Digite outro número\n")
         n = n - 10**(x-1)  
while(f >= 0 ):
    if(n - (10**f) >= 0):
        n = n - (10**f)
        print(f+1)
    else:
        f-=1