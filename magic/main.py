from maths1 import *
while True:
    print("1.overload + operator")
    print("2.overload - operator")
    print("3.overload * operator")
    print("6.overload / operator")
    print("4.overload // operator")
    print("5.Exit")

    ch= int(input("input the choice"))


    if ch ==1:
        op1=calculation()
        op2=calculation()
        op1.accept()
        op2.accept()
        print(op1+op1)
    elif ch==2:
        print(op1-op2)
    elif ch==3:
        print(op1*op2)
    elif ch==6:
        print(op1/op2)
    elif ch==4:
        print(op1//op2)   
    elif ch==5:
        break    