n=int(input("Enter the limit:"))
print("Fibanocci series is:")
def fibo(n):
    n1=0
    n2=1
    count=0
    print(n2)
    while(count<(n-1)):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        count=count+1
fibo(n)
