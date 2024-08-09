print("guess your bday month")
month=0
n=eval(input("if no is in 1,3,5,7,9,11 press 1 otherwise 0 :"))
if n==1:
    month=month+1

n1=eval(input("if no is in 2,3,6,7,10,11 press 1 otherwise 0 :"))
if n1==1:
    month=month+2

n2=eval(input("if no is in 4,5,6,7,12 press 1 otherwise 0 :"))
if n2==1:
    month=month+4

n3=eval(input("if no is in 8,9,10,11,12 press 1 otherwise 0 :"))
if n3==1:
    month=month+8

month_names=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

if 1<= month<= 12:
    print("your bday month is ",month_names[month-1 ])
else:
    print("try again ")
