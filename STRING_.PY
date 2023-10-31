# string[start:end:step_value]
# a="hello world"
# print(a[4:-2])


# b="hello world"
# print(b[6:],b[:6])


# def modify(a):
#     b=[x*2 for x in a]
#     print(b)
# def modify(a):
#     b=[x*x for x in a]
#     print(b)
# a=[1,2,3]
# modify(a)


#DOCS QUESTIONS:-

# str="hello"
# print(str[:3])


# str="myblog"
# a=6
# for i in range(len(str)):
#     print(*str[i])


# s="my"
# s1="blog"
# s2=s[:1]+s1[len(s1)-1:]
# print(s2)


# print("my"+"blog"*2)

# for i in range(2,7,2):
#     print(i*"2")


# for i in range(3,12,13):
#     print("a".upper())


# s="welcome to my site https://nayaksworld.com"
# print(s.find("come"))
# print(s.find("o"))
# print(s.find("o",5,10))


# str="nishinishi"
# print(str[13])


# str1="welcome to my blog"
# print(str1[-1])
# print(str1[9])


# str="welcome to my blog"
# for i in range(len(str)):
#     print(str[i])


# str="welcome to my blog"
# i=0
# while i <(len(str)):
#     print(str[i])
#     i+=1


# print(6+3)
# print("6"+"3")
# print("a"+"b"+"c")


# str="madhu"
# c=0
# for i in str:
#     c+=1
# print(c)
    

# str="my blog"
# for i in str:
#     print(i)
#     print(i,end="#")


# for i in range(2,5,2):
#     print(i*"@")

# for i in "amit":
#     print(i in "amit")

#******
# p="amit">"Amitabh"
# print(p)


# s="welcome to my blog"
# print(s[2:3])
# print(s[2:10])
# print(s[-2:])
# print(s[-10:-2:2])


# str="madhu"
# print(str.isalpha())


# str1="Amit"
# print(str1.isalpha())
# str2="#blog"
# print(str2.isalpha())


# str4="my 1st blog"
# print(str4.isalpha())


# s="123madhu@jha_81"
# c=0
# for i in s:
#     if i.isalpha():
#         c+=1
# print(c)

# str="my position is 1st and my freind come on 4th"
# sum=0
# for i in str:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)


# b=123
# print(b.isdigit())


# m="madhu"
# print(m.upper())

# s=input()
# l=u=0
# for i in s:
#     if i.islower():
#         l+=1
#     else:
#         u+=1
# print("lowercase=",l,"uppercase=",u)


# S="My Blog"
# print(S.upper())
# print(S.lower())
# print(S.isupper())
# print(S.islower())
# print(S.isalpha())
# print(S.isdigit())


# str=" hello world "
# print(str.lstrip())


# str="   welcome to my blog"
# print(len(str))
# print(len(str.rstrip()))
# print(len(str.rstrip()))


# str="welcome to my blog"
# print(len(str.rstrip("og")))
# print(len(str.lstrip("we")))
# print(len(str.strip("welog")))


# s2="   amit  "
# print(s2.isspace())


# s="my blog"
# print(s.capitalize())

# str="welcome-to-my-blog"
# x=str.split("-")
# print(len(x))


# str="welcome to my blog"
# x=str.title()
# print(x)


# a="mummy?papa?brother?sister?uncle"
# print(a.split())
# print(a.split("?"))
# print(a.split("?",1))
# print(a.split("?",3))
# print(a.split("?",10))
# print(a.split("?",-1))


# a="i do you do and we all do"
# print(a.replace("do","done"))


# str="welcome to my blog"
# print(str.find("o",7,10))


# s="madhu"
# print(s[::-1])


# m="madhu"
# for i in range(0,20):
#     print(m)


# s="i am happy now"
# print(s.upper())

# s="madhu"
# print(s[-3:])

# s="madhu"
# print(s[:3])



# s=input()
# s=s.title()
# s=s.split()
# string=" "
# for i in s:
#     string+=i[:-1]+i[-1].upper()+" "
# print(string)
