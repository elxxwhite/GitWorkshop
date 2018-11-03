
#A
print("[A]")
for x in range (1,11):
    for y in range(x):
        print("*", end = " ")
    print()   

print()

#B
print("[B]")
for x in range (10,0,-1):
    for y in range(x):
        print("*", end = " ")
    print()  

print()

#C
print("[C]")
for x in range (10,0,-1):
    print("  "*(10-x), end ="")
    for y in range(x):
        print("*", end = " ")     
    print()  

print()

#D
print("[D]")
for x in range (1,11):
    print("  "*(10-x), end="")
    for y in range(x):
        print("*", end = " ")
    print()   

print()
