#IF ELSE ASSIGNMENT (3):-


#1.
# a=int(input("enter a no.1"))
# b=int(input("enter a no.2"))
# c=int(input("enter a no.3"))
# if a>b:
#     max=a
#     smax=b
# else:
#     max=b
#     smax=a
# if c>max:
#     print(c,"is maximum no.")
# else:
#     print(max,"is maximum no.")



#2.
# year=int(input("enter a no."))
# month=int(input("enter a no."))
# date=int(input("enter a no."))
# if year>0:
#     if month>0:
#         if month<=12:
#             if date>0:
#                 if date<=31:
#                     print(year,month,date)
#                 else:
#                     print("invalid")
#             else:
#                 print("invalid")
#         else:
#             print("invalid")
#     else:
#         print("invalid")
# else:
#     print("invalid")



#3.
# unit=int(input("enter a unit"))
# if unit<=50:
#     bill=unit*0.50
#     print(bill+bill*0.20)
# elif unit<=150:
#     bill=(unit*0.50+(unit-50)*0.755)
#     print(bill+bill*0.20)
# elif unit<=250:
#     bill=(unit*0.50+unit*0.75+(unit-150)*1.20)
#     print(bill+bill*0.20)
# else:
#     bill=(unit*0.50+unit*0.75+unit*1.20+(unit-250)*1.50)
#     print(bill+bill*0.20)



#4.
# n=int(input("enter a electricity unit"))
# if n<=100:
#     cost=0
#     print(cost)
# elif n<=200:
#     cost=0+(n-100)*5
#     print(cost)
# else:
#     cost=500+(n-200)*10
#     print(cost)



#5.
# age=int(input("enter a age"))
# gender=(input("enter a gender"))
# days=int(input("enter a days"))
# if age>=18:
#     if age<=30:
#         if gender=="male":
#             wages=days*700
#             print("male wages",wages)
#         else:
#             wages=days*750
#             print("female wages",wages)
#     elif age<=40:
#         if gender=="male":
#             wages=days*800
#             print("male wages",wages)
#         else:
#             wages=days*850
#             print("female wages",wages)
#     else:
#         print("invalid")       
# else:
#     print("invalid")



#6.
# days=int(input("enter a days"))
# if days<=5:
#     charge=days*2
#     print("lirary charge is",charge,"rs")
# elif days<=10:
#     charge=(5*2+(days-5)*3)
#     print("library charge is",charge,"rs")
# elif days<=15:
#     charge=((5*2)+(10*3)+(days-10)*4)
#     print("library charge is",charge,"rs")
# else:
#     charge=((5*2)+(10*3)+(15*4)+(days-15)*5)
#     print("library charge is ",charge,"rs")



#7.
# amt_=int(input("enter a no."))
# total_notes=0
# if amt_>=2000:
#     notes=amt_//2000
#     amt_=amt_-(notes*2000)
#     total_notes+=notes
#     print(notes,("notes of 2000rs"))
# if amt_>=500:
#     notes=amt_//500
#     amt_=amt_-(notes*500)
#     total_notes+=notes
#     print(notes,"notes of 500rs")
# if amt_>=200:
#     notes=amt_//200
#     amt_=amt_-(notes*200)
#     total_notes+=notes
#     print(notes,"notes of 200rs")
# if amt_>=100:
#     notes=amt_//100
#     amt_=amt_-(notes*100)
#     total_notes+=notes
#     print(notes,"notes of 100rs")
# if amt_>=50:
#     notes=amt_//50
#     amt_=amt_-(notes*50)
#     total_notes+=notes
#     print(notes,"notes of 50rs")
# if amt_>=20:
#     notes=amt_//20
#     amt_=amt_-(notes*20)
#     total_notes+=notes
#     print(notes,"notes of 20rs")
# if amt_>=10:
#     notes=amt_//10
#     amt_=amt_-(notes*10)
#     total_notes+=notes
#     print(notes,"notes of 10rs")
# if amt_>=5:
#     notes=amt_//5
#     amt_=amt_-(notes*5)
#     total_notes+=notes
#     print(notes,"notes of 5rs")
# if amt_>=2:
#     notes=amt_//2
#     amt_=amt_-(notes*2)
#     total_notes+=notes
#     print(notes,"notes of 2rs")
# if amt_>=1:
#     notes=amt_//1
#     amt_=amt_-(notes*1)
#     total_notes+=notes
#     print(notes,"notes of 1rs")
# else:
#     print(total_notes,"total notes")



#8.
# a=int(input("enter a side"))
# b=int(input("enter a side"))
# c=int(input("enter a side"))
# d=int(input("enter a side"))
# i=int(input("enter a angle"))
# if a==b:
#     if b==c:
#         if c==d:
#             if i==90:
#                 print("square")
#             else:
#                 print("rhombus")
#         else:
#             print("irregular")
#     else:
#         print("irregular")
# else:
#     if a==c:
#         if d==b:
#             if i==90:
#                 print("rectangle")
#             else:
#                 print("parallelogram")
#         else:
#             print("irregular")
#     else:
#         print("irregular")



#9.
# component_1=int(input("enter a marks_1."))
# component_2=int(input("enter a marks_2"))
# percentage=((component_1+component_2)/100)*100
# if component_1>=20:
#     if component_2>=20:
#         if percentage>=45:
#             print(percentage,"pass")
#         elif percentage==44:
#             print(percentage,"moderate to pass")
#         else:
#             print(percentage,"fail")
#     else:
#         print(percentage,"technical fail")
# else:
#     print(percentage,"technical fail")

    

#10.
# salary=int(input("enter a your salary"))
# if salary>0:
#     if salary>3000:
#         print("300rs bonus")
#     elif salary>1600:
#         if salary<=3000:
#             bonus=(0.10*salary)
#             if bonus<=240:
#                 print(bonus,"rs bonus")
#             else:
#                 print("no bonus")
#         else:
#             print("no bonus")
#     elif salary<=1600:
#         bonus=(0.15*salary)
#         if bonus>=100:
#             print(bonus,"rs bonus")
#         else:
#             print("no bonus")
#     else:
#         print("no bonus")
# else:
#     print("no bonus")
        


#11.
# rockwell=int(input("enter a quantity"))
# carbon=float(input("enter a quantity"))
# tensile=int(input("enter a quantity"))
# if rockwell>50:
#     if carbon>0.7:
#         if tensile>5600:
#             print("grade 10")
#         else:
#             print("grade 9")
#     elif tensile>5600:
#         print("grade 7")
#     else:
#         print("grade 0")
# elif carbon>0.7:
#     if tensile>5600:
#         print("grade 8")
#     else:
#         print("grade 0")
# else:
#     print("grade 0")



#12.
# year=int(input("enter a year"))
# if year%4==0:
#     if year%100!=0:
#         print(year,"is leap year")
#     elif year%400==0:
#         print(year,"is leap year")
#     else:
#         print(year,"is not leap year")
# else:
#     print(year,"is not leap year")



#13.
# year=int(input("enter a year"))
# if year%100!=0:
#     if year%4==0:
#         print(year,"is leap year")
#     else:
#         print(year,"is not leap year")
# elif year%400==0:
#     print(year,"is leap year")
# else:
#     print(year,"is not leap year")



#14.
# year=int(input("enter a year"))
# if year%400==0:
#     print(year,"is leap year")
# elif year%4==0:
#     if year%100!=0:
#         print(year,"is leap year")
#     else:
#         print(year,"is not leap year")
# else:
#     print(year,"is not leap year")



#15.
# a=int(input("enter a side"))
# b=int(input("enter a side"))
# c=int(input("enter a side"))
# if a>0:
#     if b>0:
#         if c>0:
#             if (a+b+c)==180:
#                 if a>b:
#                     max=a
#                 else:
#                     max=b
#                 if c>max:
#                     max=c
#                     if max==90:
#                         print("right angle triangle")
#                 elif max==60:
#                     print("equilateral")
#                 elif max>90:
#                     print("obtuse angle")
#                 else:
#                     print("acute angle")
#             else:
#                 print("invalid")
#         else:
#             print("invalid")
#     else:
#         print("invalid")
# else:
#     print("invalid")

            

                
#16.
# a=int(input("enter a side"))
# b=int(input("enter a side"))
# c=int(input("enter a side"))
# if a+b>c:
#     if b+c>a:
#         if c+a>b:
#             if a==b:
#                 if b==c:
#                     print("equilateral triangle")
#                 else:
#                     print("isosceles triangle")
#             elif b==c:
#                 print("isosceles triangle")
#             else:
#                 print("scalene triangle")
#             if a**2+b**2==c**2:
#                 print("right angle triangle")
#             elif b**2+c**2==a**2:
#                 print("right angle triangle")
#             elif c**2+a**2==b**2:
#                 print("right angle triangle")
#             else:
#                 print("triangle")
#         else:
#             print("invalid")
#     else:
#         print("invalid")
# else:
#     print("invalid")

                

#17.
# n=int(input("enter a no."))
# if n%5==0:
#     if n%11==0:
#         print("both are divisible by",n)
#     else:
#         print("divisible by 5",n)
# elif n%11==0:
#     print("divisible by 11",n)
# else:
#     print("none divisible by",n)



#18.
# a=int(input("enter a no."))
# b=int(input("enter a no."))
# c=int(input("enter a no."))
# if a>b:
#     max=a
#     smax=b
# else:
#     max=b
#     smax=a
# if c>max:
#     print(max,"is smax")
# elif c>smax:
#     print(c,"is smax")
# else:
#     print(smax,"is smax")



#19.
# a=int(input("enter a no."))
# b=int(input("enter a no."))
# c=int(input("enter a no."))
# d=int(input("enter a no."))
# if a>b:
#     max=a
#     smax=b
# else:
#     max=b
#     smax=a
# if c>d:
#     max1=c
#     smax1=d
# else:
#     max1=d
#     smax1=c
# if max>max1:
#     if max1>smax:
#         print(max1,"is smax")
#     else:
#         print(smax,"is smax")
# elif max>smax1:
#     print(max,"is smax")
# else:
#     print(smax1,"is smax")


#MERGED 2ND MAX AND 3RD MAX:

# a=int(input("enter a no."))
# b=int(input("enter a no."))
# c=int(input("enter a no."))
# d=int(input("enter a no."))
# if a>b:
#     max=a
#     smax=b
# else:
#     max=b
#     smax=a
# if c>d:
#     max1=c
#     smax1=d
# else:
#     max1=d
#     smax1=c
# if max>max1:
#     if max1>smax:
#         print(max1,"is smax")
#     else:
#         print(smax,"is smax")
# elif max>smax1:
#     print(max,"is smax")
# else:
#     print(smax1,"is smax")

# if a>b:
#     min=b
#     smin=a
# else:
#     min=a
#     smin=b
# if c>d:
#     min1=d
#     smin1=c
# else:
#     min1=c
#     smin1=d
# if min>min1:
#     if min>smin1:
#         print(smin1,"is third max")
#     else:
#         print(min,"is third max")
# elif min1>smin:
#     print(smin,"is third max")
# else:
#     print(min1,"is third max")




#20.
# a=int(input("enter a no."))
# b=int(input("enter a no."))
# c=int(input("enter a no."))
# d=int(input("enter a no."))
# if a>b:
#     min=b
#     smin=a
# else:
#     min=a
#     smin=b
# if c>d:
#     min1=d
#     smin1=c
# else:
#     min1=c
#     smin1=d
# if min>min1:
#     if min>smin1:
#         print(smin1,"is third max")
#     else:
#         print(min,"is third max")
# elif min1>smin:
#     print(smin,"is third max")
# else:
#     print(min1,"is third max")


