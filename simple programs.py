#Armstrong number
n=input("enter the number: ")
s=0
for i in range(len(n)):
    k=n[i]
    k=int(k)**3
    s+=k
if n==str(s):
    print("ok")
else:
    print("not")


#nth fibonaucci number

n=int(input("enter the number of term : "))
a=0
b=1
i=2
while i<n:
    if n==0:
        print(a)
        break
    elif n==1:
        print(b)
    else:
        c=a+b
        a=b
        b=c
        i+=1
print(c)

#fibonaucii series

n=int(input("enter the number of term : "))
a=0
b=1
i=2

if n==0:
    print(a)
        
elif n==1:
    print(b)
    
else:
    if n!=0 and n!=1:
        print(0,end=',')
        print(1,end=',')
        while i<n:
    
            c=a+b
            a=b
            b=c
            i+=1
            print(c,end=',')


#palindrome


n=input("enter the string or number: ")
k=n[::-1]
if n==k:
    print("palindrome")
else:
    print("wrong")

#another solution

n=input("enter the string or number: ")
s=str()
for i in range(len(n)-1,-1,-1):
    s+=n[i]
if n==s:
    print("palindrome")
else:
    print("wrong")


#prime num or not

prime=False
n=int(input("enter the numer: "))
for i in range(2,n):
    if n%i==0:
        prime=True
        break
if prime:
    print("it is not prime")
else:
    print(" prime")



#second max,second min
l=[1,2,3,4,5]
l1=[l[i] for i in range(len(l)) if l[i]!=max(l) and l[i]!=min(l)]
print(max(l1),min(l1))
