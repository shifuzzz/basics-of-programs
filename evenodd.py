for i in range(1,6):
    if i==3:
        continue
    if i%2==0:
        print(i,"is even")
    else:
        if i==3:
            print(i,"is odd and middle number")
        else:
            print(i,"is odd")   
        