#1.

# n=[]
# m=int(input())
# i=0
# while i<m:
#     a=int(input())
#     n+=[a]
#     i+=1
# print(n)
# i=m-1
# g=[]
# while i>=0:
#     g+=[n[i]]
#     i-=1
# print(g)
    


#2.1

# n=int(input())
# l=[]
# i=0
# while i < n:
#     a=int(input())
#     l+=[a]
#     i+=1
# print(l)
# sum=0
# j=0
# while j<n:
#     sum+=l[j]
#     j+=1
# print("MEAN=",sum/n)


#2.2

# n=int(input())
# l=[]
# for i in range(n):
#     n=int(input())
#     l+=[n]
# print(sorted(l))
# if n%2!=0:
#     x=((n+1)/2)
#     print("MEDIAN=",x)
# else:
#     y=(((n/2)+((n/2)+1))/2)
#     print("MEDIAN=",y)


#MEDIAN#

# l=[1,4,2,3,9,7,5]
# l=[1,2,3,4,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# if len(l)%2!=0:
#     div=l[len(l)//2]
#     print(div)
# else:
#     d=l[len(l)//2-1]
#     p=l[len(l)//2]
#     median=(d+p)/2
#     print(median)



#2.3

# n=int(input())
# l=[]
# for i in range(n):
#     n=int(input())
#     l+=[n]
# print(l)
# i=0
# c=0
# while i<n:
#     c1=0
#     j=0
#     while j<n:
#         if l[i]==l[j]:
#             c1+=1
#         j+=1
#     if c<c1:
#         c=c1
#         s=l[i]
#     i+=1
# print("mode of list is=",s)



#3.

# m=int(input())
# p=int(input())
# l=[]
# i=0
# while i<m:
#     a=int(input())
#     l+=[a]
#     i+=1
# print(l)
# l2=[0]*m
# i=0
# c=0
# t=0
# while i < m:
#     if l[t]!="a":
#         c+=1
#     if c==p:
#         l2[i]=l[t]
#         l[t]="a"
#         c=0
#         i+=1
#     t=(t+1)%m
# print(l2)
    


#4.

# n=int(input())
# l=[]
# i=0
# while i<n:
#     k=int(input())
#     l+=[k]
#     i+=1
# print(l)
# l2=[]
# i=0
# while i<n:
#     c=0
#     j=i+1
#     while j<n:
#         if l[j]=="A":
#             j+=1
#             continue
#         elif l[i]==l[j]:
#             c+=1
#             l[j]="A"
#         j+=1
#     if c>0:
#         l2+=[l[i]]
#     i+=1
# print(l2)


#5.

# m=int(input())
# l=[]
# k=[]
# i=0
# while i<m:
#     a=int(input())
#     l+=[a]
#     i+=1
# print(l)
# i=0
# while i<m:
#     s=int(input())
#     k+=[s]
#     i+=1
# print(k)
# v=[]
# v+=(l+k)
# print("merged array",v)
# i=0
# while i<(m+m):
#     j=i+1
#     while j<(m+m):
#         if v[i]>v[j]:
#             v[i],v[j]=v[j],v[i]
#         j+=1
#     i+=1
# print("sorted array",v)



#6.

# s=int(input())
# a=int(input())
# l=[]
# i=0
# while i < a:
#     b=int(input())
#     l+=[b]
#     i+=1
# i=0
# while i < a:
#     j=i+1
#     while j<a:
#         if l[i]==s:
#             print("given value is equal to this element",l[i])
#             break
#         elif l[i]+l[j]==s:
#             print("given value is equal to there sum",l[i],l[j])
#             break
#         j+=1
#     i+=1



#7.2 #INTERSECTION:-

# m=[1,2,8,9,0]
# n=[1,2,4,7,8]
# intersection=[]
# i=0
# while i < len(m):
#     j=0
#     while j<len(n):
#         if m[i]==n[j]:
#             intersection+=[m[i]]
#         j+=1
#     i+=1
# print(intersection)




#7.1 # UNION #.****

# def printUnion(arr1, arr2,m,n):
# 	i, j = 0, 0
# 	while i < m and j < n:
# 		if arr1[i] < arr2[j]:
# 			print(arr1[i],end=" ")
# 			i += 1
# 		elif arr2[j] < arr1[i]:
# 			print(arr2[j],end=" ")
# 			j+= 1
# 		else:
# 			print(arr2[j],end=" ")
# 			j += 1
# 			i += 1
# 	while i < m:
# 		print(arr1[i],end=" ")
# 		i += 1

# 	while j < n:
# 		print(arr2[j],end=" ")
# 		j += 1
# arr1 = [2,3,4,5,1]
# arr2 = [1,2,3,4,5]
# m=len(arr1)
# n=len(arr2)
# printUnion(arr1, arr2, m, n)




#8.

# n=int(input())
# m=int(input())
# l=[]
# k=[]
# i=0
# while i < n:
#     a=int(input())
#     l+=[a]
#     i+=1
# j=0
# while j < m:
#     d=int(input())
#     k+=[d]
#     j+=1
# l2=[]
# l2+=(l+k)
# print(l2)
# if (n+m)%2==0:
#     j=((m+n/2)+((n+m)+1)/2)
#     print(j)
# else:
#     h=((m+n)+1)/2
#     print(h)


#9.

# h=int(input())
# j=[]
# i=0
# while i<h:
#     a=int(input())
#     j+=[a]
#     i+=1
# print(j)
# key=int(input())
# i=0
# l=h-1
# f=0
# mid=0
# while i<=l and f==0:
#     mid=(i+l)//2
#     if (key==j[mid]):
#         pos=mid+1
#         f=1
#     elif (key>j[mid]):
#         i=mid+1
#     else: 
#         l=mid-1
# if f==1:
#     print(key,"no.fount at=,",pos)
# else:
#     print(key,"no. not found")


#10.1 #BUBBLE SORT#.

# n=int(input())
# arr=[]
# i=0
# while i<n:
#     k=int(input())
#     arr+=[k]
#     i+=1
# i=0
# while i < n:
#     j=0
#     while j < (n-i-1):
#         if arr[j]>arr[j+1]:
#             (arr[j],arr[j+1])=(arr[j+1],arr[j])
#         j+=1
#     i+=1
# print("BUBBLE SORT=",arr)



#10.2 #SELECTION SORT#.

# p=int(input())
# g=[]
# i=0
# while i < p:
#     a=int(input())
#     g+=[a]
#     i+=1
# i=0
# while i < (p-1):
#     min_index=i
#     j=i+1
#     while j<(p):
#         if g[j]<g[min_index]:
#             min_index=j
#         j+=1
#     (g[i],g[min_index])=(g[min_index],g[i])
#     i+=1
# print("SELECTION SORT=",g)



#10.3 #INSERTION SORT#.

# n=int(input())
# h=[]
# i=0
# while i < n:
#     a=int(input())
#     h+=[a]
#     i+=1
# i=0
# while i<n:
#     key=h[i]
#     j=i-1
#     while j>=0 and key<h[j]:
#         h[j+1]=h[j]
#         j-=1
#     h[j+1]=key
#     i+=1
# print("INSERTION SORT=",h)


# PRACTICE:

# m=5
# l=[1,2,3,4,5]
# i=m-1
# p=[]
# while i>=0:
#     p+=[l[i]]
#     i-=1
# print(p)


# k=5
# l=[4,5,6,1,2]
# sum=0
# i=0
# while i<k:
#     sum+=l[i]
#     i+=1
# print("MEAN",sum/k)



# o=8
# h=[1,3,4,2,3,3,1,7]
# c=0
# j=0
# while j<o:
#     c1=0
#     i=0
#     while i<o:
#         if h[j]==h[i]:
#             c1+=1
#         i+=1
#     if c<c1:
#         c=c1
#         s=h[j]
#     j+=1
# print("MODE OF LIST",s)


# n=int(input())
# p=int(input())
# g=[]
# i=0
# while i<n:
#     j=int(input())
#     g+=[j]
#     i+=1
# print(g)
# l2=[0]*n
# k=0
# t=0
# c=0
# while k<n:
#     if g[t]!="a":
#         c+=1
#     if c==p:
#         l2[k]=g[t]
#         g[t]="a"
#         c=0
#         k+=1
#     t=(t+1)%n
# print(l2)




# m=int(input())
# list=[]
# i=0
# while i<m:
#     j=int(input())
#     list+=[j]
#     i+=1
# print(list)
# list2=[]
# j=0
# while j<m:
#     c=0
#     i=j+1
#     while i<m:
#         if list[i]=="a":
#             i+=1
#             continue
#         elif list[j]==list[i]:
#             c+=1
#             list[i]=="a"
#         i+=1
#     if c>0:
#         list2+=[list[j]]
#     j+=1
# print(list2)


# l=[1,2,3,7,8]
# key=int(input())
# i=0
# while i < len(l):
#     j=i+1
#     while j<len(l):
#         if l[i]==key:
#             print(l[i])
#             break
#         elif l[i]+l[j]==key:
#             print(l[i],l[j])
#             break
#         j+=1
#     i+=1


# n=8
# l=[2,5,1,3,7,9,0,4]
# i=0
# while i<n:
#     j=0
#     while j<(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
            
#         j+=1
#     i+=1
# print(l)

        

# n=8
# l=[7,1,3,2,8,9,0,6]
# i=0
# while i <(n-1):
#     mid_index=i
#     j=i+1
#     while j<n:
#         if l[j]<l[mid_index]:
#             mid_index=j
#         j+=1
#     l[i],l[mid_index]=l[mid_index],l[i]
#     i+=1
# print(l)


# n=8
# l=[3,6,7,1,2,5,6,0]
# i=0
# while i<n:
#     key=l[i]
#     j=i-1
#     while j>=0 and key<l[j]:
#         l[j+1]=l[j]
#         j-=1
#     l[j+1]=key
#     i+=1
# print(l)




