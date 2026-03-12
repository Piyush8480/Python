n1 = int(input("Enter n1 value "))
n2 = int(input("Enter n2 value "))
n3 = int(input("Enter n3 value "))
if n1>n2:
    if n1>n3:
       print("N1 is greater")
    else:
       print("N3 is greater") 
else:
    if n2>n3:
        print("N2 is greater")
    else:
        print("n3 is greater")            

# Minimum number 
if n1<n2:
    if n1<n3:
       print("N1 is smaller")
    else:
       print("N3 is smaller") 
else:
    if n2<n3:
        print("N2 is smaller")
    else:
        print("n3 is smaller")         