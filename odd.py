a=int(input("enter a limi:"))
sum=0
for i in range(0,a):
    if i%2!=0:
        sum=sum+i
print("sum of odd:",sum)