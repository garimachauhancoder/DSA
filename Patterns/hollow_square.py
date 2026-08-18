n = int(input("Enter no. of lines: "))
for j in range(n):
    print("*", end=" ")
print()

for i in range(n-2):
    print("*", end=" ")
    
    for j in range(n-2):
        print(" ", end=" ")
    print("*")

for j in range(n):
    print("*", end=" ")
print()