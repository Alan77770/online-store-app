#for i in range(1,31):
    #print(i)


n=int(input("enter the number to reverse:"))
reverse=0
temp=n
while temp>0:
    rem=temp %10
    reverse=reverse*10+rem
    temp=10
print("Reverse of {o} is {1}", format(n,reverse))    


