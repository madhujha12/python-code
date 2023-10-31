# def message():
#     print("hello madhu")
# message()


# def ask_question():
#     print("once")
# i=1
# while i<=100:
#     ask_question()
#     i+=1


# numbers=[4,56,78,9,0]
# print(max(numbers))
# print(min(numbers))


# numbers=[12,78,90,4,5,6,0]
# print(sum(numbers))


# num=[1,9,0,45,3,2,78,56,3]
# print(sorted(num))


# n=[1,2,3,9,0,6,4,3,8]
# n.reverse()
# print(n)


# def f():
#     print(2+4)
# f()


# def iseven():
#     if (12%2==0):
#         print("even number")
#     else:
#         print("odd number")
# iseven()



# def my_function(name):
#     print(name+" hello")
# my_function("madhu")
# my_function("priya")
# my_function("aman")


# def add():
#     a=int(input("enter a no."))
#     b=int(input("enter a no."))
#     c=a+b
#     print("addition=",c)
# add()
# add()


# a=[1,4,5,6,9,2,0]
# print(len(a))

# def say(name):
#     print("hello",name)
#     print("Are you fine or not?")
# say("madhu,priya,amisha,nishi.")


# def add_numbers(m,n):
#     print("I will be add those numbers")
#     print(m+n)
# add_numbers(2,8)


# def add_numbers(m,n):
#     print("I will be add those numbers")
#     print(m+n)
# k=12
# l=67
# add_numbers(k,l)


# def say_hello_language(name,language):
#     if language=="hindi":
#         print("Namaste",name)
#         print("KAISE H AAP")
#     elif language=="maithili":
#         print("khus rhu",name)
#         print("ahan kehen chii buaa")
#     else:
#         print("hello",name)
#         print("how are you?",name)
# say_hello_language("priya","maithili")
# say_hello_language("madhu","maithili")
# say_hello_language("amisha","hindi")
# say_hello_language("nishi","french")
        


# def ask_name(name1,name2,name3):
#     print("HELLO", name1)
#     print("ALAH HAFIZ",name2)
#     print("NAMASTE",name3)
# ask_name("Madhu","Priya","Aman")
# ask_name("Amisha","Nishi","Priya")


# def chocolates(*variety):
#     for i in variety:
#         print("I LOVE " + i)
# chocolates("DAIRY MILK","5 STAR","KIT KAT")


# def chocolates(*variety):
#     i=0
#     while i<len(variety):
#         print("I LOVE "+ variety[i])
#         i+=1
# chocolates("SNACKERS","KIT KAT","MUNCH")



# def attendence(name,status="absent"):
#     print(name,"is",status,"today")
# attendence("madhu", "present")
# attendence("priya")
# attendence("aman","present")



# def info(name,founder):
#     print("My name is",name)
#     print("I am the founder of", founder)
# info("Abhishek","navgurukul")


# def value(a,b=20):
#     if a>20 and b>20:
#         print("true")
#     else:
#         print("false")
# value(30)


# def add(n,m):
#     print(n+m)
# add(1,5)


# def fun(l1,l2):
#     for i in range(len(l1)):
#         sum=l1[i]+l2[i]
#         print(sum, end= " ")
# list1=[12,34,56,89]
# list2=[13,45,23,78]
# fun(list1,list2)


# def fun(l,L):
#     i=0
#     while i<(len(l)):
#         print(l[i]+L[i],end=" ")
#         i+=1
# fun([1,5,6,78,34],[89,5,4,34,8])


# def check_even(m,n):
#     if (m%2==0 and n%2==0):
#         print("BOTH ARE EVEN NUMBERS")
#     else:
#         print("BOTH ARE NOT EVEN NUMBERS")
# check_even(20,30)
# check_even(4,9)


# def even_check(l1,l2):
#     for i in range(len(l1)):
#         if(l1[i]%2==0 and l2[i]%2==0):
#             print("BOTH INTEGERS ARE EVEN")
#         else:
#             print("BOTH INTEGERS ARE NOT EVEN")
# l1=[12,34,56,78,9]
# l2=[2,4,3,6,7]
# even_check(l1,l2)


# def even_check(l1,l2):
#     i=0
#     while i<(len(l1)):
#         if(l1[i]%2==0 and l2[i]%2==0):
#             print("BOTH INTEGERS ARE EVEN")
#             i+=1
#         else:
#             print("BOTH INTEGERS ARE NOT EVEN")
#             i+=1
# l1=[12,34,56,78,9]
# l2=[2,4,3,6,7]
# even_check(l1,l2)


# def add(num_1,num_2):
#     num_sum=(num_1+num_2)
#     return num_sum
# num_sum=add(3,6)
# print(num_sum)


# def add_num(num_x,num_y):
#     num_sum=(num_x+num_y)
#     return num_sum
# sum1=add_num(23,67)
# print(sum1)
# sum2=add_num(560,23)
# a=12
# b=134
# sum3=add_num(a,b)
# print(sum2)
# print(sum3)
# number_a=add_num(20,40)/add_num(5,1)
# print(number_a)



# def add_num(num,num2):
#     num_sum=num+num2
#     print(num_sum)
# sum4=add_num(4,5)
# print(sum4)
# print(type(sum4))


# def add_(a,b):
#     num_add=(a+b)
#     print(num_add)
# add_(2,1)


# def add_num(num_a,num_b):
#     num_sum=num_a+num_b
#     print("Hellooo..")
#     return num_sum
#     num_sum=num_a+num_b
#     print("hii...")
#     return num_sum
# sum=add_num(12,5)
# sum=add_num(1,7)
# print(sum)



# def menu(day):
#     if day=="monday":
#         return "butter chicken"
#     elif day=="tuesday":
#         return "momos"
#     else:
#         return "pizza"
#     print("will i be able to print?:-(")
# mon_menu=menu("monday")
# tue=menu("tuesday")
# wed=menu("wednesday")
# print(tue)
# print(wed)
# print(mon_menu)


# def menu(day):
#     if day=="monday":
#         food="dal,chawal"
#     elif day=="tuesday":
#         food="kheer,puri"
#     else:
#         food="matar paneer"
#     # print("when I eat ?")
#     return food
#     print("but i am not sure will print?:-(")
# print("when I eat ?")
# print(menu("monday"))
# print(menu("wednesday"))
# print(menu("tuesday"))


# def calculator(num_1,num_2,operation):
#     if (operation=="add"):
#         print(num_1+num_2)
#     elif (operation=="sub"):
#         print(num_1-num_2)
#     elif (operation=="divide"):
#         print(num_1/num_2)
#     elif (operation=="multiply"):
#         print(num_1*num_2)
#     else:
#         print("invalid request")
# calculator(14,2,"add")
# calculator(14,2,"sub")
# calculator(14,2,"multiply")
# calculator(14,2,"divide")


# def calculator(num_1,num_2,operation):
#     if (operation=="add"):
#         c=(num_1+num_2)
#         return c
#     elif (operation=="sub"):
#         c=(num_1-num_2)
#         return c
#     elif (operation=="divide"):
#         c=(num_1/num_2)
#         return c
#     elif (operation=="multiply"):
#         c=(num_1*num_2)
#         return c
#     else:
#         print("invalid request")
# a=calculator(14,2,"add")
# print(a)
# a=calculator(14,2,"sub")
# print(a)
# a=calculator(14,2,"multiply")
# print(a)
# a=calculator(14,2,"divide")
# print(a)
# a=calculator(14,2,"mnm")



# def calculator(num_1,num_2,operation):
#     l=[]
#     if (operation=="add"):
#         print(num_1+num_2)
#     elif (operation=="sub"):
#         print(num_1-num_2)
#     elif (operation=="divide"):
#         print(num_1/num_2)
#     elif (operation=="multiply"):
#         for i in range(len(num_2)):
#             mul=num_1[i]*num_2[i]
#             l+=[mul]
#         print(l)
#     else:
#         print("invalid request")
# l1=[10,20,30,40]
# l2=[50,60,70,80]
# calculator(l1,l2,"multiply")



# def calculator(num_1,num_2,operation):
#     l=[]
#     if (operation=="add"):
#         for i in range(len(num_1)):
#             add=num_1[i]+num_2[i]
#             l+=[add]
#         print(l)
#     elif (operation=="sub"):
#         for i in range(len(num_1)):
#             sub=num_1[i]-num_2[i]
#             l+=[sub]
#         print(l)
#     elif (operation=="divide"):
#         for i in range(len(num_1)):
#             div=num_1[i]/num_2[i]
#             l+=[div]
#         print(l)
#     elif (operation=="multiply"):
#         for i in range(len(num_2)):
#             mul=num_1[i]*num_2[i]
#             l+=[mul]
#         print(l)
#     else:
#         print("invalid request")
# l1=[10,20,30,40]
# l2=[50,60,70,80]
# calculator(l1,l2,"multiply")
# calculator(l1,l2,"add")
# calculator(l1,l2,"sub")
# calculator(l1,l2,"divide")


# def f1():
#     s="I LOVE NAVGURUKUL"
#     return s
# def f2():
#     n="I LOVE NG"
#     return n
# a=f1()
# m=f2()
# print(m)
# print(a)


# def f1():
#     s="I LOVE BIO"
#     print(s)
#     def f2():
#         print(s)
#     f2()
# f1()



# def first_function():
#     s="I LOVE INDIA"
#     def second_():
#         print(s)
#     second_()
# first_function()


# def first_function():
#     s="i love india"
#     def second_():
#         s="my name is jack"
#         print(s)
#     second_()
#     print(s)
# first_function()


# def distance_(km):
#     if km<=20:
#         print("close")
#     elif km<50:
#         print("median")
#     else:
#         print("far")
# distance_(30)


#Assignment questions:

#1.
# l=[12,89,90,45]
# print(max(l))


#2.
# l=[8,2,30,7]
# print(sum(l))


#3.
# l=[8,2,3,-1,7]
# p=1
# i=0
# while i<len(l):
#     p*=l[i]
#     i+=1
# print("product=",p)


#4.
# string="1234abcd"
# print(string[-1::-1])


#5.
# def fac_(num):
#     p=1
#     i=1
#     while i<=num:
#         p*=i
#         i+=1
#     print("product=",p)
# fac_(4)


#6.
# def range_(u,l,n):
#     if n>=l and n<=u:
#         print("yes")
#     else:
#         print("no")
# range_(10,5,6)
    

#7.
# def name_(name):
#     i=0
#     upper=0
#     lower=0
#     while i<(len(name)):
#         if "A"<=name[i]<="Z":
#             upper+=1
#         elif "a"<=name[i]<="z":
#             lower+=1
#         i+=1
#     print("NO. OF LOWER CASE=",lower,"NO.OF UPPER CASE=",upper)
# name_("The Quick Brown Fox Jumps Over The Lazy Dog")        


#8.
# def digits_(l):
#     unique_list=[]
#     for i in l:
#         if i not in unique_list:
#             unique_list.append(i)
#         i+=1
#     print(unique_list)
# digits_([1,2,3,3,3,4,4,5,5,6,7,8])


#9.
# def num_(n):
#     i=1
#     c=0
#     while i<=n:
#         if n%i==0:
#             c+=1
#         i+=1
#     if c==2:
#         print("yes")
#     else:
#         print("no")
# num_(3)


#10.
# def numbers_(l):
#     l1=[]
#     i=0
#     while i<len(l):
#         if l[i]%2==0:
#             l1.append(l[i])
#         i+=1
#     print(l1)
# numbers_([1,2,3,4,5,6,7,8])



#11.
# def numbers_(n):
#     i=1
#     sum=0
#     while i<=n//2:
#         if n%i==0:
#             sum+=i
#         i+=1
#     if sum==n:
#         print("yes")
#     else:
#         print("no")
# numbers_(8)



#12.
# def str(a):
#     s=a[-1::-1]
#     if s==a:
#         print("yes, string is pallindrome")
#     else:
#         print("no,string is not pallindrome")
# str("bob")


#14.
# def pan_():
#     flag=0
#     str="my name is madhu"
#     alphabet="abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in str:
#             flag=1
#     if flag==0:
#         print("panagram")
#     else:
#         print("not panagram")
# pan_()


#16.
# def num():
#     l=[]
#     i=1
#     while i<=30:
#         l.append(i*i)
#         i+=1
#     print(l,end="")
# num()


# print(ord("A"))


#17.
# def hyp_(a):
#     b=a.split("-")
#     c=sorted(b)
# #    print("-".join(c))****
#     for i in range(len(c)):
#         if i==3:
#             print(c[i],end="")
#         else:
#             print(c[i],end="-")
# hyp_("red-yellow-green-blue")


#19.
# def mum_():
#     s="we are freinds"
#     def num_():
#         s="we are happy now"
#         return s
#     a=num_()
#     print(a)
#     print(s)
# mum_()

 
#LAMBDA FUNCTION#
# x=lambda a:a+10
# print(x(5))

#SUM#
# def num_(a,b):
#     sum=a+b
#     return sum
# v=num_(2,3)
# print(v)

#subtract#
# def num_(x,y):
#     sub=x-y
#     return sub
# f=num_(3,1)
# print(f)


#multiply#
# def mul_(m,n):
#     multiply=m*n
#     return multiply
# m=int(input())
# n=int(input())
# print(mul_(m,n))


#divide#
# def div_(j,k):
#     div=j/k
#     return div
# j=int(input())
# k=int(input())
# print("ANSWER=",div_(j,k))



#factorial

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))



#fibnocci series:
# def fib(n):
#     x=0
#     y=1
#     z=0
#     for i in range(n):
#         x=y
#         y=z
#         z=x+y
#         print(z)
# fib(5)



###theory###
# local variable= inside the function using print
# global variable=outside the function using print
#argument=(in value when called funtion)
#parameter=(in variable in upper parenthesis)
    

                    
        