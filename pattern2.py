n=5
# for i in range(1,n+1):
i=1
while(i<=n):
    j=1
    while(j<=n-1):
        if i==n:
            print("* ",end="")
        else:    
            print("",end="")      
        j=j+1
    if j==n:
        print("*")
    i=i+1      