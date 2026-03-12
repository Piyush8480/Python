# mydict ={
#     "name" :"Sumit",
#     "profession" :"SDE-1",
#     "empid" : 2003

# }
# print(mydict)
# print(type(mydict))

mydict ={
    101: "Sumit",
    102: "Sahil",
    "103": "Raut",
    "104": "Makide",
    101: "Hello",
    104: "World"

}
print(mydict)

# The 101 key updates its value 

# access values with the help of key 

a = mydict[102]
print(a)

mydict[101] ="Hieeeee"
print(mydict)

#prints keys 
# for x in mydict:
#     print(x)

#printing values 

# for x in mydict.values():
#     print(x)

#printing both 
# x will point to the keys and y points value 
# for x,y in mydict.items():
#     print(x,y)

# adding new key and value in dictionary 
mydict["Mobile no :"]=8459281934
print(mydict)

mydict.pop(101)
print(mydict)