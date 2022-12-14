sum=0
ls=[1,2,3,4,5]
for i in range(0,len(ls)):
    sum=sum+ls[i]
print("Sum of elements is:",sum)

..........................OR...................
 
    
    def sum_list(items):
        sum_numbers=0
        for x in items :
            sum_numbers+=x
        return sum_numbers
    print(sum_list[1,2,6])
