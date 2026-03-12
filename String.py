name ="sumitraut"
# data =['a','e','i','o','u']
# vowels =0
# con =0

# for i in name:
#     if i in data:
#         vowels +=1
#     else:
#         con +=1    

# print(vowels)
# print(con)

vow=0
conson=0

for i in name:
    if(i=='a' or i=='e' or i=='o' or i=='u' or 'i'):
        vow +=1
    else:
        conson +=1

print(vow)
print(conson)