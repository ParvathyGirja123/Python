l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
a=[]
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x ]
print(a)
