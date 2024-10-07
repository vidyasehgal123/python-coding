x=int(input("enter the number"))
y=len(x)
sum=0
temp = x
while temp>0 :
    digit= temp%10
    sum+=digit*digit*digit
    temp=temp//10

if sum==x:
    (print("this is armstrong"))


