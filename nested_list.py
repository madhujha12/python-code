#HOW TO PRINT MATRICES:

# r=int(input())
# c=int(input())
# matrix=[]
# for i in range(r):
#     a=[]
#     for j in range(c):
#         n=int(input())
#         a+=[n]
#     matrix+=[a]
# print(matrix)



#1.adding matrices:

# a=[[2,1,3],
# [3,4,5]]
# b=[[4,3,1],
# [7,2,1]]
# row=len(a)
# col=len(a[0])
# c=[0]*row
# i=0
# while i<row:
#     j=0
#     p=[0]*col
#     while j<col:
#         p[j]=a[i][j]+b[i][j]
#         j+=1
#     c[i]=p
#     i+=1
# print(c)


#1.adding matrices:

# x=[[1,2,3],[2,3,4],[3,4,5]]
# y=[[1,2,3],[2,3,4],[4,5,6]]
# row=len(x)
# col=len(x[0])
# c=[0]*row
# for i in range(row):
#     p=[0]*col
#     for j in range(col):
#         p[j]=x[i][j]+y[i][j]
#     c[i]=p
# print(c)



#2.

# A    = 	[[2, 4, 1],
# 	 [8, 0, -1],
# 	 [1, -4, 0]]
# B   =    [[8, 0, 3],
# 	 [2, -5, 7],
# 	 [3, -1, 5]] 
# row=len(A)
# col=len(A[0])
# c=[0]*row
# for i in range(row):
#     p=[0]*col
#     for j in range(col):
#         p[j]=A[i][j]-B[i][j]
#     c[i]=p
# print(c)



#3.
# A    = 	[[2, 4, 1],
# 	 [8, 0, -1],
# 	 [1, -4, 0]]
# B   =    [[8, 0, 3],
# 	 [2, -5, 7],
# 	 [3, -1, 5]] 
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         for k in range(len(B)):
#             result[i][j]+=A[i][k]*B[k][j]
# for r in result:
#     print(r)



#4.
# A    = 	[[2, 4, 1],
# 	 [8, 0, -1],
# 	 [1, -4, 0]]
# row=len(A)
# col=len(A[0])
# c=[0]*col
# for i in range(row):
#     p=[0]*row
#     for j in range(col):
#         p[j]=A[j][i]     
#     c[i]=p
# print(c)


    
#5.
# k=0
# b=""
# for i in range(1,11):
#     n=int(input())
#     k+=1
#     b+=str(n)
#     if k==9:
#         pass
#     elif k%3==0:
#         b+="-"
# print(b)


#6.
# n=int(input())
# l=[]
# for i in range(n):
#     a=int(input())
#     l+=[a]
# print(l)
# print("new list=",[l[-1]]+l[0:-1])



#7.

# r=int(input())
# c=int(input())
# matrix=[]

# for i in range(r):
#     a=[]
#     for j in range(c):
#         n=int(input())
#         a.append(n)
#     matrix.append(a)
# f=0
# for i in range(r):
#     for j in range(c):
#         if i==j and matrix[i][j]!=1:
#             f=1
#             break
#         elif i!=j and matrix[i][j]!=0:
#             f=1
#             break 
# if f==0:
#     print("identity matrix is=",matrix)
# else:
#     print("not identity matrix=",matrix)




#8.

# r=int(input())
# c=int(input())
# matrix=[]

# for i in range(r):
#     a=[]
#     for j in range(c):
#         n=int(input())
#         a.append(n)
#     matrix.append(a)
# f=0
# for i in range(r):
#     for j in range(c):
#         if i==j and matrix[i][j]==0:
#             f=1
#             break
#         elif i!=j and matrix[i][j]!=0:
#             f=1
#             break
# if f==0:
#     print("diagonal matrix=",matrix)
# else:
#     print("not diagonal matrix=",matrix)



#9.

# r=int(input())
# c=int(input())
# matrix=[]

# for i in range(r):
#     a=[]
#     for j in range(c):
#         n=int(input())
#         a.append(n)
#     matrix.append(a)
# f=0
# sum=0
# for i in range(r):
#     for j in range(c):
#         if i==j :
#             sum+=matrix[i][j]
# print(matrix)
# print("SUM OF DIAGONAL MATRIX ELEMENTS=",sum)       




#10,11.

# def max_min(arr):
#     max=arr[0][0]
#     min=arr[0][0]
#     for i in range(r):
#         for j in range(c):
#             if max<arr[i][j]:
#                 max=arr[i][j]
#             if min>arr[i][j]:
#                 min=arr[i][j]
#     print("maximum=",max,"minimum=",min)
# r=int(input())
# c=int(input())
# matrix=[]
# for i in range(r):
#     a=[]
#     for j in range(c):
#         n=int(input())
#         a.append(n)
#     matrix.append(a)
# print(matrix)
# max_min(matrix)




#12.
# r=int(input())
# c=int(input())
# matrix=[]
# for i in range(r):
#     a=[]
#     for i in range(c):
#         m=int(input())
#         a.append(m)
#     matrix.append(a)
# print("MATRIX",matrix)
# search_ele=int(input())
# f=0
# row=0
# col=0
# for i in range(r):
#     for j in range(c):
#         if matrix[i][j]==search_ele:
#             f=1
#             row=i
#             col=j
# if f==1:
#     print("Position of Search Element ",search_ele," is (",row,",",col,")")
# else:
#     print("GIVEN ELEMENT IS NOT FOUND IN MATRIX",search_ele)


# PRACTICE:


# r=int(input())
# c=int(input())
# mat=[]
# for i in range(r):
#     a=[]
#     for j in range(c):
#         n=int(input())
#         a+=[n]
#     mat+=[a]
# print(mat)


# a=[[2,1,3],
# [3,4,5]]
# b=[[4,3,1],
# [7,2,1]]
# row=len(a)
# col=len(a[0])
# c=[0]*row
# for i in range(row):
#     p=[0]*col
#     for j in range(col):
#         p[j]=a[i][j]+b[i][j]
#     c[i]=p
# print(c)



# A    = 	[[2, 4, 1],
# 	 [8, 0, -1],
# 	 [1, -4, 0]]
# B   =    [[8, 0, 3],
# 	 [2, -5, 7],
# 	 [3, -1, 5]] 
# res=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         for k in range(len(B)):
#             res[i][j]+=A[i][k]*B[k][j]
# for r in res:
#     print(r)




# A = 	[[2, 4, 1],
# 	 [8, 0, -1],
# 	 [1, -4, 0]]
# row=len(A)
# col=len(A[0])
# R=[0]*col
# for i in range(row):
#     p=[0]*row
#     for j in range(col):
#         p[j]=A[j][i]
#     R[i]=p
# print(R)


# l=0
# j=""
# for i in range(1,11):
#     m=int(input())
#     l+=1
#     j+=str(m)
#     if l==9:
#         pass
#     elif l%3==0:
#         j+="-"
# print(j)


# l=[0]
# n=int(input())
# for i in range(n):
#     j=int(input())
#     l+=[j]
# print(l)
# print("NEW LIST",[l[-1]]+l[0:-1])



# r=int(input())
# c=int(input())
# final=[]
# for i in range(r):
#     p=[]
#     for j in range(c):
#         l=int(input())
#         p+=[l]
#     final+=[p]
# g=0
# for i in range(r):
#     for j in range(c):
#         if i==j and final[i][j]!=1:
#             g=1
#             break
#         elif i!=j and final[i][j]!=0:
#             g=1
#             break
# if g==0:
#     print("IDENTITY MATRIX",final)
# else:
#     print("NOT IDENTITY MATRIX", final)




# r=int(input())
# c=int(input())
# final=[]
# for i in range(r):
#     p=[]
#     for j in range(c):
#         l=int(input())
#         p+=[l]
#     final+=[p]
# g=0
# for i in range(r):
#     for j in range(c):
#         if i==j and final[i][j]!=0:
#             g=1
#             break
#         elif i!=j and final[i][j]==0:
#             g=1
#             break
# if g==0:
#     print("IDENTITY MATRIX",final)
# else:
#     print("NOT IDENTITY MATRIX", final)



# def max_min(arr):
#     max=arr[0][0]
#     min=arr[0][0]
#     for i in range(r):
#         for j in range(c):
#             if max<arr[i][j]:
#                 max=arr[i][j]
#             if min>arr[i][j]:
#                 min=arr[i][j]
#     print("MAXIMUM",max,"MINIMUM",min)
# r=int(input())
# c=int(input())
# k=[]
# for i in range(r):
#     g=[]
#     for j in range(c):
#         j=int(input())
#         g+=[j]
#     k+=[g]
# print(k)
# max_min(k)





# def solve(n):
#    for i in range(n-1,-1,-1):
#       for j in range(i):
#          print(end="--")
#       for j in range(n-1,i,-1):
#          print(chr(j+97),end="-")
#       for j in range(i,n):
#          if j != n-1:
#             print(chr(j+97),end="-")
#          else:
#             print(chr(j+97),end="")
#       for j in range(2*i):
#          print(end="-")
#       print()
#    for i in range(1,n):
#       for j in range(i):
#          print(end="--")
#       for j in range(n-1,i,-1):
#          print(chr(j+97),end="-")
#       for j in range(i,n):
#          if j != n-1:
#             print(chr(j+97),end="-")
#          else:
#             print(chr(j+97),end="")
#       for j in range(2*i):
#          print(end="-")
#    print()

# n = 5
# solve(n)




# r=int(input("enter a row"))
# c=int(input("enter a column"))
# row=len(r[0])

