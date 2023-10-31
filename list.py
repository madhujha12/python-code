#LIST ASSIGNMENT CODE:-

#1.
# natural_no=[0]*20
# n=20
# i=0
# while i<n:
#     natural_no[i]=i+1
#     i+=1
# print (natural_no)

#2.
# l=[0]*5
# i=0
# while i<5:
#     a=input("enter a names")
#     l[i]=a
#     i+=1
# print(l)



#3.
# l=[5,4,9,2,1,0]
# i=5
# while i>=0:
#     print(l[i],end=',')
#     i-=1



#4.
# l=[5,4,9,2,1,0]
# i=5
# while i>=0:
#     print(l[i-1],end=',')
#     i-=2



#5.
# i=int(input("enter a no."))
# l=["a",1,2,5,"b","q"]
# a=len(l)
# n=0
# while i>n:
#     print(l[a-1])
#     i-=1
#     a-=1



#6.
# l=[1,2,3,4,5,6,7]
# n=int(input("enter a no"))
# i=0
# c=0
# while i<7:
#     if l[i]==n:
#         c+=1
#         i+=1
#     else:
#         i+=1
# if c>0:
#     print("yes")
# else:
#     print("no")



#7.
# l=[0]*7
# c=0
# i=0
# while i<7:
#     a=int(input("enter a no."))
#     l[i]=a
#     i+=1
# j=0
# while j<6:
#     if l[j+1]-l[j]==1:
#         c+=1
#     j+=1
# if c==6:
#     print("consecutive no.")
# else:
#     print("not consecutive no.")




# def fun():
#     l=[112,320,230,431,233,231,432,232,412,598]
#     a=sorted(l)
#     l3=[]
#     l4=[]
#     for i in range(len(l)-1):
#         if len(l3)>=5:
#             if a[i+1]-a[i]==1:
#                 l4+=[a[i],a[i+1]]
#         elif a[i+1]-a[i]==1:
#             l3+=[a[i],a[i+1]]
#     dup_=(set(l3))
#     l2=[]
#     for i in dup_:
#         l2+=[i]
#     print([l2,l4])
# fun()




#8.
# n=int(input("enter a no."))
# l=[0]*n
# sum=0
# i=0
# while i<n:
#     num=int(input("enter a no."))
#     l[i]=num
#     sum+=num
#     i+=1
# print(sum)
# print(sum/n)



#9.
# n=int(input("enter a no."))
# num=int(input("enter  a no."))
# l=[0]*n
# c=0
# i=0
# while i<n:
#     a=int(input("enter a no."))
#     l[i]=a
#     if l[i]==num:
#         c+=1
#     i+=1
# print(c)



#10.
# n=int(input("enter a no."))
# l=[0]*n
# i=0
# c_P=0
# c_n=0
# while i<n:
#     num=int(input("enter a no."))
#     l[i]=num
#     i+=1
# i=0
# while i<n:
#     if l[i]>0:
#         c_P+=1
#     elif l[i]<0:
#         c_n+=1
#     i+=1
# print("positive",c_P,"negative",c_n)



#11.
# n=int(input("enter a no."))
# a=[0]*n
# i=0
# while i<n:
#     num=int(input("enter a no."))
#     a[i]=num
#     i+=1
# i=0
# l=[]
# while i<n:
#     c=0
#     j=i+1
#     while j<n:
#         if a[j]=="A":
#             j+=1
#             continue
#         elif a[i]==a[j]:
#             c+=1
#             a[j]="A"
#         j+=1
#     if c>0:
#         l.append(a[i])
#         i+=1
#     else:
#         i=i+1
# print(l)
    


#12.
# n=int(input("enter a no."))
# l=[0]*n
# i=0
# a=0
# while i<n:
#     l[i]=a+2
#     a+=2
#     i+=1
# print(l)


#13.
# n=int(input("enter a no."))
# l=[0]*n
# a=1
# i=0
# while i<n:
#     l[i]=a
#     a+=2
#     i+=1
#print(l)


#14.
# n=int(input("enter a no."))
# l=[]
# i=1
# while i*i<=n:
#     if n%i==0:
#         l+=[i]
#         l+=[n//i]
#     i+=1
#print(l)



#15.***********
# n=int(input("enter a no."))
# l=[0]*n
# j=2
# while j<=n:
#     c=0
#     i=2
#     while i*i<=j:
#         while j%i==0:
#             c=1
#             if c==0:
#                 l[i]=i
#         i+=1
#     j+=1
#     if c==0:
#         l[i]=i
#     else:
#         j+=1
# print(l)



#16.
# n=int(input("enter a no."))
# l=[]
# i=1
# while i<=n:
#     j=1
#     sum=0
#     while j*j<i:
#         if i%j==0:
#             sum+=j
#             sum+=i//j
#         j+=1
#     if (sum-i)==i:
#         l.append(i)
#     i+=1
# print(l)




#17.
# num=int(input("num = "))
# l=[]
# i=2
# while i<=num:
#     sum=0
#     j=i
#     len1=len(str(j))
#     while j>0:
#         a=j%10
#         sum+=a**len1
#         j//=10
#     if sum==i:
#         l+=[i]
#         i+=1
#     else:
#         i+=1
# print(l)
    


#18.
# n=int(input("enter a no."))
# i=1
# while i<=n:
#     j=1
#     p=1
#     l=[]
#     while j<=i:
#         p*=j
#         l.append(p)
#         j+=1
#     i+=1
# print(l)



#19.
# l=[0]*10
# i=0
# even=0
# odd=0
# while i<10:
#     num=int(input("enter a no."))
#     if num%2==0:
#         even+=1
#         l[i]=num
#         i+=1
#     else:
#         odd+=1
#         i+=1
# print("ODD=",odd,"EVEN=",even)

    

    
#20.
# l=[0]*10
# i=0
# sum_even=0
# sum_odd=0
# while i<10:
#     n=int(input("enter a no."))
#     l[i]=n
#     i+=1
# else:
#     i=0
#     while i<len(l):
#         if i%2==0:
#             sum_even+=l[i]
#             i+=1
#         else:
#             sum_odd+=l[i]
#             i+=1
#     print("SUM_EVEN=",sum_even,"SUM_ODD=",sum_odd)



#21.
# n=int(input("enter a no."))
# l=[0]*n
# i=0
# while i<n:
#     names=input("names")
#     l[i]=names
#     i+=1
# print(l)



#22,23.
# n=int(input("enter a no."))
# l=[0]*n
# i=0
# while i<n:
#     names=input("names")
#     l[i]=names
#     i+=1
# i=0
# l1=[0]*n
# j=n
# while n>i:
#     l1[i]=l[j-1]
#     j-=1
#     i+=1
# print(l1)




#24.
# n=int(input("enter a no."))
# l=[0]*n
# i=0
# while i<n:
#     num=input("enter a no.")
#     l[i]=num
#     i+=1
# i=0
# max=0
# max=l[i]
# while i<n:
#     if l[i]>max:
#         max=l[i]
#         i+=1
#     else:
#         i+=1
# print("max = ",max)



#25.
# n=100
# l=[0]*n
# i=0
# while i<n:
#     l[i]=i+1
#     i+=1
# l1=[0]*n
# i=0
# j=n
# while i<n:
#     l1[i]=l[j-1]
#     j-=1
#     i+=1
# print(l1)



#26.
# n=int(input("enter a no."))
# l=[0]*n
# i=0
# while i<n:
#     a=int(input("enter a no."))
#     l[i]=a
#     i+=1
# min=l[0]
# max=l[0]
# sum=0
# j=0
# while j<n:
#     if l[j]<min:
#         min=l[j]
#         sum+=l[j]
#     elif l[j]>max:
#             max=l[j]
#             sum+=l[j]
#     else:
#         sum+=l[j]
#     j+=1        
# print("MIN = ",min,"MAX = ",max,"AVERAGE = ",sum/n)



#PRACTICE**

#27.
# m=int(input("enter a no."))
# l1=["1","2","A","7","q"]
# n=0
# while n<m:
#     print(l1[n],end=" ")
#     n+=1


#28.
# n=int(input("enter a no."))
# l=[]
# i=0
# while i<n:
#     a=int(input("enter a no."))
#     if a%2==0:
#         l+=[a]
#     i+=1
# print(l)


#29.
# N=int(input("enter a no."))
# l=[]
# i=0
# while i<N:
#     a=int(input("enter a no."))
#     l+=[a]
#     i+=1
# sum_o=0
# sum_e=0
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         sum_e+=l[i]
#     else:
#         sum_o+=l[i]
#     i+=1
# print("sum of even no.",sum_e,"sum of odd no.",sum_o)


#DOCS QUESTIONS:-#

#1.
# grocery_list=["flour","cheese","carrots"]
# for i in range(len(grocery_list)):
#     print(grocery_list[i])


#2.
# a=[10,"madhu",4]
# a.remove("madhu")
# print(a)


