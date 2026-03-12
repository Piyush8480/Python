# print (float(3.14))
# print(float(True))
# print(float(False))
# print(float("4"))
# print(float(3))

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# # print(complex("Piyush"))
# print(complex(5,-3))
# print(complex(True,False))

# print(bool(0))
# print(bool(False))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2))
# print(bool(0+0))
# print(bool(-1))
# print(bool(True))

# # WAP for simple intrest
# # principle amount = pxrxt/100
# principle = 10000
# roi = 10
# time = 1
# simint = principle *roi*time/100
# print("Simple Interest : ",simint)

# # WAP to accept the centigrate temp aand convert it to farenheit temperature
# # T(oF) = (T(oC) × (9/5)) + 32
# centigrate = 100
# farenheit = centigrate * (9/5) + 32
# print(farenheit,"Farenheit")

# # Swapping of two values
# val1 = 1
# val2 = 2
# temp = val1
# val1 = val2
# val2 = temp
# print(val1,val2)

# val1 = 1
# val2 = 2
# val1 = val1+val2
# val2=val1-val2
# val1 = val1-val2
# print(val1,val2)

# # WAP to enter height of user in ffeet and convert it into inch and centimeter
# h = 6
# inch = h * 12
# cm = inch * 2.54
# print(inch,"inch",cm,"cm")

# # WAP to reverse number
# num = 1234567
# original_num = num
# reversed_num = 0

# while num > 0:
#     digit = num % 10           
#     reversed_num = reversed_num * 10 + digit  
#     num = num // 10             
# print(f"Original number: {original_num}")
# print(f"Reversed number: {reversed_num}")


# # -------------COLLECTION DATATYPE----------------# DAY-2

# mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])


# mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
# mylist.append('harsh')
# mylist.append("laxman")
# print(mylist)


# mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
# mylist.insert(1,"sanket")
# print(mylist)


# mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
# mylist.remove("sandip")
# print(mylist)


# mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
# newlist = mylist.copy() #cloning
# print(mylist)
# print(newlist)


# mylist = [['prashant','jha'],['85.56'],[440022,'yyy']]
# print("Example of multidimensional list:")
# print(mylist)
# # Accessing elements
# print(mylist[0][0])   # prashant
# print(mylist[0][1])   # jha
# print(mylist[1][0])   # 85.56
# print(mylist[2][0])   # 440022
# print(mylist[2][1])   # yyy


# list1 = ["prashant","jha"]
# print(list1*2) #it will print 2 times
# list2 = [50,25.50]
# print(list1+list2)

# list2 = [50,25.50,"prashant"]
# del list2[2]
# print(list2)

# list2 = [50,25.50,"prashant"]
# list2.clear()
# print(list2)

# name = "prashant"
# print(name)
# myname = list(name) #typecasting
# print(myname)


# # SORTING EXAMPLE
# mylist = [44,22,77,0,9,88]
# mylist.sort()
# print(mylist)

# math = 10
# physics = 10
# print(id(math),id(physics))


# # ALISING
# mylist = [44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# # LOOPING
#operator- membership operator [1]in [2]not in
# name = 'pashant'
# print('2'in name)
# print('2' not in name)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i*2,"|",i*3, "|",i*4)

# # WAP ato accept any digit and check the po,neg and zero
# no = int(input('Enter any digit-->'))
# if no>0:
#     print('positive')
# if no<0:
#     print('negative')
# if no==0:
#     print('zero')


# #  WAP to accept days and check the working days and weekend
# days = input("enter your day-->")
# if days == 'saturday' or days == 'sunday':
#     print('weekend')
# else:
#     print('working day')


# WAP to accept three paper marks and calculate total,percentage and if percentage is greater then equal to 60 then he is eligible for placement
# WAP to accept three paper marks and calculate total, percentage
# and check eligibility for placement
m1 = int(input("Enter marks of paper 1: "))
m2 = int(input("Enter marks of paper 2: "))
m3 = int(input("Enter marks of paper 3: "))
# calculating total
total = m1 + m2 + m3
# calculating percentage
percentage = (total / 300) * 100
print("Total marks =", total)
print("Percentage =", percentage)
# checking eligibility
if percentage >= 60:
    print("Eligible for placement")
else:
    print("Not eligible for placement")