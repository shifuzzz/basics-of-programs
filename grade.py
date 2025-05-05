total_mark=float(input("enter total percentage:"))
if total_mark >=90:
    print("grade A")
elif total_mark >= 80 and total_mark <= 89:
    print("grade B")
elif total_mark >= 70 and total_mark <= 79:
    print("grade C") 
elif total_mark >= 60 and total_mark <= 69:
    print("grade D")
elif total_mark >= 50:
    print("grade E")
else:
    print("FAILED!!!")