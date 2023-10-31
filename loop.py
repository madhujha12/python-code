#LOOP ASSIGNMENT CODE:-


#1.
# n=int(input("enter a no."))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum",sum)



#2.
# n=15
# sum=0
# i=1
# a=2
# while i<=n:
#     sum+=a
#     a+=2
#     i+=1
# print(sum,"sum of first even natural no.")



#3.
# count=0
# n=2
# sum=0
# while sum<1000:
#     sum+=n
#     n+=2
#     count+=1
# print(sum,"=sum",",",count,"=count")



#4.
# n=100
# while n>0:
#     if n%7==0:
#         print(n,"is divisible by 7")
#         n-=1
#     else:
#         n-=1

    

#5
# n=int(input("enter a no."))
# i=1
# p=1
# while i<=n:
#     p=p*i
#     i+=1
# print("product of n no.",p)




#6.
# lower=int(input("enter a no."))
# upper=int(input("enter a no."))
# while lower<=upper:
#     if lower%2==0:
#         if lower%7==0:
#             print(lower)
#             lower+=1
#         else:
#             lower+=1
#     else:
#         lower+=1



#7.
# i=1
# sum=0
# while i<=9:
#     if i%3==0:
#         sum=sum+i*i
#         i+=1
#     else:
#         i+=1
# print(sum,"sum")



#8.
# n=int(input("enter a no."))
# i=1
# f=1
# sum=0
# while i<=n:
#     sum+=f/i
#     i+=1
# print(sum,"sum")




#9.
# lower=int(input("enter a no."))
# upper=int(input("enter a no."))
# p=int(input("enter a no."))
# q=int(input("enter a no."))
# sum=0
# while lower<=upper:
#     if lower%p==0:
#         if lower%q!=0:
#             sum+=lower
#             lower+=1
#         else:
#             lower+=1
#     else:
#         lower+=1
# print("sum=",sum)



#10.
# a=int(input("enter a no.1"))
# b=int(input("enter a no.2"))
# i=1
# while a>b:
#     max=a
#     min=b
# else:
#     max=b
#     min=a
# if i<=min:
#     if min%i==0:
#         if max%i==0:
#             hcf=i
#             i+=1
#         else:
#             i+=1
#     else:
#         i+=1
# lcm=(a*b)/hcf
# print("HCF",hcf , "LCM",lcm)

#10.
# n1=int(input("enter 1st no."))
# n2=int(input("enter 2nd no."))
# product=n1*n2
# while n2>0:
#     r=n1%n2
#     n1=n2
#     n2=r
# hcf=n1
# lcm=product//hcf
# print("hcf=",hcf,"lcm=",lcm)


#11.
# N=int(input("enter a no."))
# sum=0
# rem=0
# while N>0:
#     rem=N%10
#     N=N//10
#     sum+=rem
# print("SUM=",sum)



#12.
# n=int(input("enter a no. "))
# rem=0
# while n>0:
#     rem=rem*10+(n%10)
#     n=n//10
# print("REVERSE=",rem)



#13.
# n=int(input("enter a no."))
# i=1
# while i<=(n//i):
#     if n%i==0:
#         print("factor of n",i,n//i)
#         i+=1
#     else:
#         i+=1



#14.
# n=int(input("enter a no."))
# ori=n
# sum=0
# i=1
# while i<n:
#     if n%i==0:
#         sum+=i
#         i+=1
#     else:
#         i+=1
# if sum==ori:
#     print("perfect no.",n)
# else:
#     print(n," is not perfect no.")



#15.
# n=int(input("enter a no."))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count+=1
#         i+=1
#     else:
#         i+=1
# if count==2:
#     print(n,"is prime no.")



#15.
# n=int(input("enter a no."))
# i=2
# flag=1
# while i*i<=n:
#     if n%i==0:
#         flag=0
#     i+=1
# if flag==0:
#     print(n,"is not prime no.")
# else:
#     print(n,"is prime no.")



#16(a).
# x=int(input("enter a no."))
# n=int(input("enter a no."))
# i=1
# sum=0
# while i<=n:
#     sum+=(x**i)/i
#     i+=1
# print("sum",sum)



#16(b).*****
# x=int(input("enter a no."))
# n=int(input("enter a  no."))
# i=2
# term=x
# sum=0
# while i<=n:
#     term=term*((-x**2)*(2*i-3)/2*i-1)
#     sum+=term
# print(sum)



#17.
# n=int(input("enter a no."))
# i=1
# j=1
# sum=0
# total_sum=0
# while i<=n:
#     a=5*j
#     sum+=a
#     total_sum+=sum
#     j*=10
#     i+=1
# print(total_sum)



#18.
# i=1
# while i<=5:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     else:
#         print()
#     i+=1



#19.
# n=int(input())
# i=2
# while i<n:
#     j=2
#     s=1
#     while j*j<=i:
#         if i%j==0:
#             s=s+j
#             if j!=i/j:
#                 s=s+i/j
#                 j+=1
#         j+=1
#     if s==i:
#         print(i,"is perfect no.")
#         i+=1
#     i+=1
    
    


#20.
# i=100
# while i<=999:
#     s=0
#     n=i
#     while n>0:
#         r=n%10
#         n=n//10
#         s+=r**3
#     if s==i:
#         print(i,"armstrong no.")
#         i+=1
#     i+=1



#21.
# i=100
# while i<=999:
#     s=0
#     n=i
#     while n>0:
#         r=n%10
#         n=n//10
#         f=1
#         while r>0:
#             f=f*r
#             r=r-1
#         else:
#             s=s+f
#     if s==i:
#         print(i,"factorial.")
#         i+=1
#     i+=1




#22.*************
# n=int(input("enter a no."))
# i=1
# while i<=n:
#     j=1
#     k=1
#     while j<=(n+i-1):
#         while i+j<=n:
#             print("",end="")
#             j+=1
#         else:
#             print(k,end="")
#         if j<5:
#             k+=1
#             j+=1
#         k-=1
#         j+=1
#     else:
#         print()
#     i+=1



#23(a).*****
# i=1
# while i<=5:
#     a=1
#     if a<=5-i:
#         print(" ",end="")
#         a+=1
#     else:
#         k=1
#     if k<=i:
#         print("*",end="")
#         k+=1
#     else:
#         print()
#         i+=1



#23(a).
# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end="")
#         j+=1
#     print(i*"*",end="")
#     print()
#     i+=1



#23(b).
# i=1
# while i<=4:
#     j=1
#     while j<=4-i:
#         print(" ",end="")
#         j+=1
#     print(i*"*",end="")
#     print((i-1)*"*")
#     print()
#     i+=1


#23(c).
# i=1
# while i<=3:
#     j=1
#     while j<=7:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



#23(d).
# i=1
# while i<=3:
#     j=1
#     if i==2:
#         print("*",end="")
#         b=1
#         while b<=1:
#             print(" ",end="")
#             b+=1
#         print()
#         i+=1
#     while j<=8:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



#23(e).
# i=1
# while i<=5:
#     j=1
#     while j<=6-i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



#24.
# n=int(input("enter a no."))
# sum=0
# mul=1
# if n%2==0:
#     while n>0:
#         sum+=(n%10)
#         n//=10
#     print(sum)
# else:
#     while n>0:
#         mul*=(n%10)
#         n//=10
#     print(mul)   



# 25.
# n=int(input("enter a no."))
# hcf=int(input("enter a no."))
# i=1
# while i<n:
#     a=int(input("enter a no."))
#     if a>0:
#         r=hcf%a
#         hcf=a
#         a=r
#     i+=1
# print(hcf)



#26.
# n=int(input("enter a no."))
# i=1
# mx=float("-inf")
# mn=float("inf")
# while i<=n:
#     a=int(input("enter a no."))
#     if a>mx:
#         mx=a
#     if a<mn:
#         mn=a
#     i+=1
# print("mn=",mn,"mx=",mx)



#27.
# n=int(input("enter a no."))
# mx=float("-inf")
# mn=float("-inf")
# i=0
# while i<n:
#     a=int(input("enter a no."))
#     if a>mx:
#         smx=mx
#         mx=a
#     elif a>smx:
#         smx=a
#     i+=1
# print("smax=",smx)



#28.
# n=int(input("enter a no."))
# mx=float("-inf")
# smx=float("-inf")
# tmx=float("-inf")
# i=1
# while i<=n:
#     a=int(input("enter a no."))
#     if a>mx:
#         tmx=smx
#         smx=mx
#         mx=a
#     elif a>smx:
#         tmx=smx
#         smx=a
#     elif a>tmx:
#         tmx=a
#     i+=1
# print("tmax=",tmx)



#29.
# n=int(input("enter a no."))
# c=0
# i=2
# while c<n:
#     flag=1
#     j=2
#     while j*j<=i:
#         if i%j==0:
#             flag=0
#         j+=1
#     else:
#         if flag==1:
#             print(i)
#             c+=1
#             i+=1
#         else:
#             i+=1



#30.
# n=int(input("enter a no."))
# sum=0
# i=2
# while i<n:
#     flag=1
#     j=2
#     while j*j<=i:
#         if i%j==0:
#             flag=0
#         j+=1
#     else:
#         if flag==1:
#             sum+=i
#             i+=1
#         else:
#             i+=1
# print(sum)



#31.
# n=int(input("enter a no."))
# i=2
# while n>1:
#     while n%i==0:
#         print(i)
#         if n%i==0:
#             n=n/i
#         i+=1
#     else:
#         i+=1



#32.
# n=int(input("enter a no."))
# a=0
# b=1
# c=0
# i=1
# while i<=n:
#     a=b
#     b=c
#     c=a+b
#     i+=1
#     print(c)



#33.**********
# i=0
# lhs=(i-2)**2+(i-1)**2+i**2
# rhs=(i+1)**2+(i+2)**2
# while lhs==rhs:
#     print(i-2,i-1,i,i+2)
#     if lhs>rhs:
#         i+=1




# n=int(input())
# i=1
# while i<n:
#     print(i*"*")
#     i+=1



##pretty number###
#ENDING OR EXISTING 2,3,9#