list= [7,9,2,3,4]
r=int(len(list))
n=int(0)
a=int(0)

nl=int(input("Qué número busca? "))
for i in range(0,r):
    if nl==list[n]:
        print("El numero esta en la lista")
        a=1
    n=n+1
if a!=1:
    print("el número no esta en la lista")

