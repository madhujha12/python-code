#printing both key and value:

# dict={"madhu":18, "priya":21}
# for x,y in dict.items():
#     print(x,y)

#printing only key:

# dict={"ram":"fifth standard","shyam":"fourth standard"}
# for x in dict:
#     print(x)
    
#printing only value:
# dict={"ram":"fifth standard","shyam":"fourth standard"}
# for x in dict:
#     print(dict[x])

# a={1:2,2:4,3:2,4:8,5:10,"year":2023}
# b={"":2,6"":4}
# c={1:2,2:4,3:6,4:8,0:10}
# print(len(a)) #5
# print(any(b))#false
# print(all(a)) #true
# print(all(c)) #false
# print(sorted(c)) #in list(only keys)
# print(a.keys()) # all keys
# print(a.values()) #all values
# print(a.items()) # both keys and values
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(a.get(5)) #none
# print(a.get(5,12)) #default (12)
# print(a.pop(2))
# print(a) #4
# print(a.pop(12)) #key error
# print(thisdict.popitem())
# print(thisdict) # last key value remove
# a.update(thisdict)
# print(a)


#SEARCHING KEY IN DICTIONARY:-
# stu_info={}
# while True:
#     inf=("please enter your id and name also with separated comma or Q")
#     if inf=="Q":
#         break
#     id,name = inf.split(',')
#     stu_info.update({id:name})
# for x,y in stu_info.items():
#     print(x,y)
# key=int(input())
# if key in stu_info:
#     print("key=",key,"value=",stu_info[key])
# else:
#     print("GIVEN KEY IS NOT FOUND",key)



###DICTINARIES ASSIGNMENT###

#1.
# dict={1:"madhu",2:"priya",3:"aman"}
# dict.update({4:"anita"})
# print(dict)



#2.
# d={}
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# d.update(dict1)
# d.update(dict2)
# d.update(dict3)
# print(d)



#3. doubt=items
# dict={1:2,4:5,6:7}
# key=int(input("enter a key"))
# if key in dict.keys():
#     print("yes,key is existing")
# else:
#     print("no,key is not existing")


#4.
# dict={5:"madhu",4:"priya",3:"aman",2:"anita",1:"naveen"}
# for i,j in dict.items():
#     print({i,j})
# for i in dict:
#     print(i,dict[i])


#5.
# sam_dict=int(input("enter a no."))
# d={}
# for i in range(1,sam_dict+1):
#     d[i]=i*i
# print(d)


#6.remove key
# dict={1:1,2:4,3:9,4:16}
# del dict[1]
# print(dict)


#7.
# col=["blue","green","red","brown"]
# no_=[1,2,3,4]
# col_dict=dict(zip(col,no_))
# print(col_dict)


#8.sorting
# col={"blue":1,"green":2,"red":3,"brown":4}
# for key in sorted (col):
#     print(key,":",col[key])
    

#9.
# col={"blue":1,"green":2,"red":3,"brown":4}
# max=float("-inf")
# min=float("inf")
# for i in col:
#     if col[i]>max:
#         max=col[i]
#     if col[i]<min:
#         min=col[i]
# print(max,min)
    



#10.
# my_dict={}
# if len(my_dict)==0:
#     print("THE DICTINARY IS EMPTY")
# else:
#     print("THE DICTINARY IS NOT EMPTY")


#11.
# dict1={"a":100,"b":200,"c":300,"d":900}
# dict2={"b":300,"c":200,"a":400,"g":000}
# new_dict=dict2
# for i,j in dict1.items():
#     if i in dict2:
#         new_dict[i]=j+dict2[i]
#     else:
#         new_dict[i]=j
# print("the new dict is",new_dict)


#12.***
# from itertools import product
# d={"1":["a","b"],"2":["c","d"]}
# for x,y in product (*d.values()):
#     print(x+y)



#13.***
# dic=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]
# sum=0
# for i in  dic:
#     for j in dic.values():



#14.
# str=input()
# output=[]
# l1=[]
# for i in range(97,123):
#     c=0
#     j=chr(i)
#     for l in str:
#         if l==j:
#             c+=1
#     if c>0:
#         output+=[j]
#         l1+=[c]
# d=dict(zip(output,l1))
# print(d)


    
#15.
# dict={"p 01" : "DBMS","P 02" : "OS","P 0 3" : "SOFT COMPUTING"}
# dic={k.replace(' ',''): v for k, v in dict.items()}
# print(dic)
    


#16.
# dict={5:"madhu",4:"priya",3:"aman",2:"anita",1:"naveen"}
# for i in dict.keys():
#     print(i,end=" ")
# print()
# for i in dict.values():
#     print(i,end=" ")
# print()
# for i,j in dict.items():
#     print(i,j,end=" ")
# print(dict.keys())
# print(dict.values())
# print(dict.items())



#17.
# dict={"c1" : "RED","C2" : "GREEN","C3" :"None" }
# dic={key:value for (key,value)in dict.items()if value is not None}
# print(dic)


#18.
# grade={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print("marks greater than 170")
# final={key:value for key,value in grade.items()if value>=170}
# print(final)



#19.
# w_h={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 
# 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# print("height and weight greater than 6ft and 70kg ")
# final={key:value for key,value in w_h.items()if w_h[0]>=6.0 and w_h[1]>=70 }
# print(final)




#19.
# def filter_data(students):
#     result = {k: s for k, s in students.items() if s[0] >=6.0 and s[1] >=70}
#     return result    
 
# students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# print("Original Dictionary:")
# print(students)
# print("Height > 6ft and Weight> 70kg:")
# print(filter_data(students))


#20.
# def dic(col_):
#     final={}
#     for i,j in col_:
#         final.setdefault(i,[]).append(j)
#     return final
# col_=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# print(dic(col_))


#21.
#22.
# mark={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# def list(marks):
#     keys = marks.keys()
#     vals = zip(*[marks[k] for k in keys])
#     final = [dict(zip(keys, v)) for v in vals]
#     return final

# marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# print(list(marks))


#23.
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92,
# 'Science': 88}]
# def test(lst, marks):
#     result = [d[marks] for d in lst if marks in d]
 
#     return result

# marks = [{'Math': 90, 'Science': 92}, 
#          {'Math': 89, 'Science': 94}, 
#          {'Math': 92, 'Science': 88}]
# subj="science"
# print(test(marks,subj))

# subj="math"
# print(test(marks,subj))



# def test(lst, marks):
#     result = [d[marks] for d in lst if marks in d]
 
#     return result

# marks = [{'Math': 90, 'Science': 92}, 
#          {'Math': 89, 'Science': 94}, 
#          {'Math': 92, 'Science': 88}]
# subj = "Science"
# print("\nExtract a list of values from said list of dictionaries where subject =",subj)
# print(test(marks, subj))

# subj = "Math"
# print("\nExtract a list of values from said list of dictionaries where subject =",subj)
# print(test(marks, subj))




### dict1={5:"madhu",4:"priya",3:"aman",2:"anita",1:"naveen"}
# dict1={"d":100,"e":200,"f":300}
# dic={"m":100,"k":200,"l":300}
# dict2={"a":100,"b":200,"c":300}
# ###dict2={1:"m",2:"p",3:"a",4:"a",5:"n"}
# final=dict(** dict1,** dic,** dict2)
# print(final)


#o/p=python
# print("python".center(0))


#o/p=0 1 2
# x=(i for i in range(3))
# for i in x:
#     print(i)


#o/p=nothing is printed
# for i in "":
#     print(i)



# n=input("enter a string")
# dic={}
# for i in n:
#     j=i
#     c=0
#     for p in n:
#         if j==p:
#             c+=1
#     if c>0:
#         dic[i]=c
# print(dic)
    


# def col(n):
#     dict={}
#     for i,j in n:
#         dict.setdefault(i,[]).append(j)
#     return dict
# col_=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# print(col(col_))







