# # for i in range(0,5):
# #     print(" ".join([chr(65+i)]*(i+1)))
# for i in range(65,70):
#      for j in range(65,i+1):
#           print(chr(i),end=" ")
#      print()
# limit=int(input("enter the limit:"))
# for i in range(limit):
#      for j in range(i+1):  
#           print(chr(65+i),end=" ")
#      print()

limit=int(input("enter the limit:"))
for i in range(65, 65+limit):
     for j in range(65, i+1):  
          print(chr(i),end=" ")
     print()