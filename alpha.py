# for i in range(0,5):
#     print(" ".join([chr(65+i)]*(i+1)))
for i in range(65,70):
    for j in range(65,i+1):
         print(chr(i),end=" ")
    print()