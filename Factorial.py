n=int(input("Ingresa un numero para calcular su factorial: "))
f=int(n)
r=int(n-1)
for i in range(0,r):
    f=f*r
    r=r-1
print(f)   
