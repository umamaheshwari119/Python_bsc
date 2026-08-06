a=10
b=20
x=30 
a<b 
print(x) 

a=int(input("Enter First Number:"))   
b=int(input("Enter Second Number:"))   
c=int(input("Enter Third Number:"))   
min=a if a<b and a<c else b if b<c else c   
print("Minimum Value:",min)  

a=int(input("Enter First Number:"))   
b=int(input("Enter Second Number:"))   
c=int(input("Enter Third Number:"))   
max=a if a>b and a>c else b if b>c else c
print("Maximum Value:",max)