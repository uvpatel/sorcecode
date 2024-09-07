a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

if(a >b and a>c):
    print("a is gretest")

elif(b >c and b>a):
    print("b is gretest") 
elif(c > a and c> b):
    print("c  is gretest") 
elif(a==b):
    print("a and b is gretest")
elif(b==c):
    print("c and b is gretest")
elif(c==a):
    print("a and c is gretest")
elif(a==b and b==c and c==a):
    print("a and b and c is greatest and equal")

else:
    print("Something went wrong")