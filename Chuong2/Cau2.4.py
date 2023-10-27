a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
S=float((a+b+c)/2)
import math 
X=((S*(S-a)*(S-b)*(S-c)))
S=math.sqrt(X)
print("Dien tich= ",S)